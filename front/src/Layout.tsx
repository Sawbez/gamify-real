import { Outlet, Link } from "react-router-dom";
import React from "react"; // Ensure React is in scope when using JSX
import { User } from "./schema";

const Layout = ({ userInfo }: {
  userInfo: [User | null, React.Dispatch<React.SetStateAction<User | null>>]
}) => {
  const [userInfoVal, setUserInfo] = userInfo;

  return (
    <>
      <nav>
        <ul>
          {/* Safely render username if userInfoVal is not null */}
          {userInfoVal && <p>{userInfoVal.username}</p>}

          <li>
            <Link to="/" className="text-blue-600">Home</Link>
          </li>
          {/* Conditional rendering based on whether userInfoVal is not null */}
          {userInfoVal ? (
            <p>Hello, {userInfoVal.username}</p>
          ) : (
            <>
              <li>
                <Link to="/signin" className="text-blue-600">Sign in LLLLLLLLLLLL</Link>
              </li>
              <li>
                <Link to="/signup" className="text-blue-600">Signup</Link>
              </li>
            </>
          )}
        </ul>
      </nav>

      <Outlet />
    </>
  );
};

export default Layout;
