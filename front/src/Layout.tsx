import { Outlet, Link } from "react-router-dom";
import { Dispatch, SetStateAction } from "react";
import { User } from "./schema";


const Layout = ({ userInfo }: {
  userInfo: [User | null, React.Dispatch<React.SetStateAction<User | null>>]
}) => {
  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/" className="text-blue-600">Home</Link>
          </li>
          {(() => {
            if (userInfo[0]) {
              return (
                <p>Hello, {userInfo[0].username}</p>
              )
            } else {
              return (
                <>
                  <li>
                    <Link to="/signin" className="text-blue-600">Sign in</Link>
                  </li>
                  <li>
                    <Link to="/signup" className="text-blue-600">Signup</Link>
                  </li>
                </>
              )
            }
          })()}
        </ul>
      </nav>

      <Outlet />
    </>
  )
};

export default Layout;
