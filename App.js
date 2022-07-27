import './App.css';
import MainPage from "./resources/mainpage/mainpage";
import {Routes,Route} from "react-router-dom"
import Contactus from "./resources/contact/contactus";
import LoginPage from "./resources/loginpage";
import SignupPage from "./resources/signup";

function App() {
  return (

      <div style={{
          backgroundColor: `gray`,
          height: '110vh',
          width: '100vw'
      }}>
              <Routes>
                  <Route  path="/" element={<MainPage/>}/>
                  <Route  path='about' element={<Contactus/>}/>
                  <Route  path='loginpage' element={<LoginPage/>}/>
                  <Route  path='signup' element={<SignupPage/>}/>
              </Routes>

      </div>

  );
}

export default App;
