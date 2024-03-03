import { Outlet, Link } from "react-router-dom";
import { Dispatch, SetStateAction } from "react";
import { User } from "./schema";


const Layout = ({signedin, userInfo }: {
  signedin: boolean;
  userInfo: User | null;
}) => {

  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/" className="text-blue-600">Home</Link>
          </li>
          { signedin ? (<p></p>):(
          <li>
            <Link to="/signin" className="text-blue-600">sign in</Link>
          </li>
          )}
          <li>
            <Link to="/Signup" className="text-blue-600">Signup</Link>
          </li>
          
        </ul>
      </nav>

      <Outlet />
    </>
  )
};

export default Layout;
