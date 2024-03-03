import { Outlet, Link } from "react-router-dom";


const Layout = () => {
  


  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/" className="text-blue-600">Home</Link>
          </li>
          <li>
            <Link to="/signin" className="text-blue-600">Login</Link>
          </li>
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