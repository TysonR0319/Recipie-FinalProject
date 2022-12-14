import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { LoginUser } from "../Request/user.js";
import { Link, Navigate, useNavigate } from "react-router-dom";
import "../../styles/login.css";

export const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  let navigate = useNavigate();
  const { actions } = useContext(Context);

  const userLogin = async () => {
    try {
      const user = {
        username: username,
        password: password,
      };
      const response = await LoginUser(user);
      const data = await response.json();
      if (response.status === 200) {
        actions.setToken(data.access_token, data.user_id);
        console.log(data);
        localStorage.setItem("token", data.access_token);
      }
    } catch (err) {
      console.log("Login error: ", err);
    } finally {
      navigate("/");
    }
  };

  return (
    <div className="text-center container col-5 outter-form">
      <h1 className="mb-4">Login</h1>
      <div className="container">
        <input
          type="text"
          value={username}
          className="login-input p-3 form-control mt-8"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          value={password}
          type="password"
          className="login-input p-3 mb-2 mt-3 form-control"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          type="submit"
          className="log-btn btn-grad mb-2 mt-3"
          onClick={() => {
            userLogin();
          }}
        >
          Login
        </button>
        <Link to="/register">
          <button type="submit" className="log-btn btn-grad mb-2 mt-3">
            Register
          </button>
        </Link>
      </div>
    </div>
  );
};
