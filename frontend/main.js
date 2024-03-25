import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';

ReactDOM.render(
  <App baseUrl={'http://localhost:####/api.rsc'} user={'USER_NAME_HERE'} pass={'AUTHTOKEN_HERE'} />, 
  document.getElementById('app')
);