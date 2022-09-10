import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./View/home";

import { FormPage } from "./View/form";
import { Register } from "./View/register.js";
import { Login } from "./View/login.js";
import { Navbar } from "./component/navbar";
import injectContext from "./store/appContext";

import { Favorite } from "./View/favorite.js";
import { MealType } from "./View/mealType.js";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  return (
    <div>
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          <Navbar />
          <Routes>
            <Route element={<Home />} path="/" />
            <Route element={<FormPage />} path="/Formpage" />
            <Route element={<Register />} path="/register" />
            <Route element={<Login />} path="/login" />
            <Route element={<Favorite />} path="/favorite" />
            <Route element={<MealType />} exact path="/mealType" />
            <Route element={<h1>Not found!</h1>} />
          </Routes>
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
