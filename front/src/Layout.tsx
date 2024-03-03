import React from 'react';
import { Link } from 'react-router-dom';

class Layout extends React.Component {
  render() {
    return (
      <div>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/signin">SignIn</Link></li>
            <li><Link to="/signup">SignUp</Link></li>
          </ul>
        </nav>
      </div>
    );
  }
}

export default Layout;