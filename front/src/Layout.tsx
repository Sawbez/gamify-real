import { Outlet, Link } from "react-router-dom";
import { Dispatch, SetStateAction } from "react";


const Layout = ({setSignedIn: Dispatch<SetStateAction>,signedin: Boolean}) => {
  


  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/signin">Login</Link>
          </li>
          <li>
            <Link to="/Signup">Signup</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
  )
};

export default Layout;