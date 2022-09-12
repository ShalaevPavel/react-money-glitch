import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import Modal from './Modal/modal';


function App() {

  const [result, setResult] = useState(50000);
  
  const [ModelActive, setModelActive] = useState(true);

  return (
    <div className='App'>
      <h1>
        <h2 className='text_1'>Infinity money glitch</h2>
        <button onClick={ (setModelActive(true))}>-</button>
        <h1>{result}$</h1>
        <button onClick={() =>setResult((prevCount) => prevCount + 100)}>+</button>

      </h1>



    <Modal active={ModelActive} SetActive={setModelActive} />
     </div>
  );
}

export default App;


 {/* 
//       <h2>
//        <Animal color="red" type1="fox" age={10}/>
//        <Animal color="grey" type1="elephant" age={50}/>
//        <Animal color="black" type1="cat" age={6}/>
//        <Animal color="white" type1="whale" age={20}/>
//       </h2> */}