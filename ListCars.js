import React, { useEffect, useState } from "react";
import axios from 'axios';
import Swal from 'sweetalert2';
import withReactContent from 'sweetalert2-react-content';
import { show_popup } from "../funtions";

const ListCars = () => {
    const url = "http://127.0.0.1:5000/cars";
    const [cars, setCars] = useState([]);
    const [id, setId] = useState('');
    const [nombre, setNombre] = useState('');
    const [model, setModel] = useState('');
    const [doors, setDoors] = useState('');

    useEffect(() => {
        getCars();
    }, []);

    const getCars = async () => {
        const dataresponse = await axios.get(url);
        console.log(dataresponse.data);
        setCars(dataresponse.data.cars);
    }


        return (
            <div>
              <table>
                <thead>
                  <tr>
                    <td>No.</td>
                    <td>Nombre</td>
                    <td>Modelo</td>
                    <td>Puertas</td>
                  </tr>
                </thead>
                <tbody>
                  {cars.map((car, index) => (
                    <tr key={index + 1}>
                      <td>{index + 1}</td>
                      <td>{car.name}</td>
                      <td>{car.model}</td>
                      <td>{car.doors}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
          
};

export default ListCars;
