import {Routes,Route,BrowserRouter} from 'react-router-dom';
import ListCars from './components/ListCars';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<ListCars></ListCars>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
