import { Outlet, Link } from "react-router-dom";
import { Dispatch, SetStateAction } from "react";
import { User } from "./schema";


const Layout = ({ setSignedIn, signedin, userInfo }: {
  setSignedIn: Dispatch<SetStateAction<boolean>>;
  signedin: boolean;
  userInfo: User | null;
}) => {



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
