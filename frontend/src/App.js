import React, { Component } from "react";
import axios from "axios"; 
import "./App.css"; 
 
class App extends Component { 
  state = { 
    value1: "", 
    value2: "", 
    value3: "", 
    value4: "", 
    value5: "",
    prediction: null, 
    error: null, 
  }; 
 
  handleChange = (e) => { 
    this.setState({ 
      [e.target.name]: e.target.value, 
    }); 
  }; 
 
  handleSubmit = (e) => { 
    e.preventDefault(); 
    const { value1, value2, value3, value4, value5 } = this.state; 
 
    axios.post("http://127.0.0.1:8000/", { 
        v1: value1, 
        v2: value2, 
        v3: value3, 
        v4: value4, 
        v5: value5 
      }) 
      .then((response) => { 
        this.setState({ prediction: response.data.prediction, error: null }); 
      }) 
       
  }; 
 
  render() { 
    const { value1, value2, value3, value4, value5, prediction, error } = this.state; 
 
    return ( 
      <div id="demo"> 
        <h1 className="heading">OBESITY LEVEL PREDICTION</h1>
        <form onSubmit={this.handleSubmit}>
          <div className="App">
            <div className='inputbox'>
              <p className="input-label">HEIGHT</p>
              <input type="number" name="value1" value={value1} onChange={this.handleChange} placeholder="Height"/><br/>
              <p className="input-label">WEIGHT</p>
              <input type="number" name="value2" value={value2} onChange={this.handleChange} placeholder="Weight"/><br/>
              <p className="input-label">FAMILY HISTORY WITH OVERWEIGHT</p>
              <input type="number" name="value3" value={value3} onChange={this.handleChange} placeholder="Family History with Overweight"/><br/>
              <p className="input-label">FREQUENCY OF CONSUMPTION OF VEGETABLES</p>
              <input type="number" name="value4" value={value4} onChange={this.handleChange} placeholder="Frequency of Consumption of Vegetables"/><br/>
              <p className="input-label">AGE BIN MINMAX</p>
              <input type="number" name="value5" value={value5} onChange={this.handleChange} placeholder="Age Bin Minmax"/><br/>
            </div><br/>
            <button type="submit" className="button">Predict</button>
          </div>
        </form> 

        {prediction !== null && ( 
          <div style={{ textAlign: 'center' }}>
            <h2 className="prediction-heading">OBESITY LEVEL</h2> 
            <h2 className="prediction">{prediction}</h2>
          </div>
        )} 
        {error && <div>Error: {error}</div>} 
      </div> 
    ); 
  } 
} 
 
export default App;