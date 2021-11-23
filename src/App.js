import React, {useState} from 'react';
import './App.css';
import Select from './component/Select';
import Main from './component/Main';
import Write from './component/Write';
import Save from './component/Save';
import Warning from './component/Warning'
import {BrowserRouter, Route, Routes} from 'react-router-dom';

function App() {
  

  return (
    
    
    <BrowserRouter>
    
    <div className="App">
      <Routes> 
        <Route exact path = '' element = {<Main/>}/>
      </Routes>

      <Routes>
        <Route exact path = '/select' element={<Select/>}/>
      
      </Routes>
      
      <Routes>
        <Route exact path = '/write' element={<Write/>}/>
      
      </Routes>

      <Routes>
        <Route exact path = '/save' element={<Save/>}/>
      
      </Routes>

      <Routes>
        <Route exact path = '/warning' element={<Warning/>}/>
      
      </Routes>

      
    </div>
    </BrowserRouter>
  );
}

export default App;
