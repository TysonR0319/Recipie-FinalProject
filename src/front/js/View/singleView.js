import React, { useEffect, useState } from "react";
import Col from "react-bootstrap/Col";
import { Context } from "../store/appContext";
import "../../styles/singleView.css";
import { useParams } from "react-router-dom";
import { useContext } from "react";

export const SingleView = () => {
  const id = useParams().id;
  const [recipe, setRecipe] = useState(null);
  const { store, actions } = useContext(Context);

  useEffect(() => {
    fetch(`${process.env.BACKEND_URL}/api/recipe/${id}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then((result) => result.json())
      .then((data) => {
        setRecipe(data);
      })
      .catch((error) => console.log(error));
  }, []);

  console.log(`List ${store.ingredientList}`);
  return recipe == null ? (
    "loading"
  ) : (
    // This is the section with the title, description, times, serving and favorite heart
    <div className="singleView container">
      <div id="introBox" className="container">
        <div className="title font-weight-bold">{recipe.title}</div>
        <p className="author">{recipe.credit}</p>
        <p className="description">{recipe.description}</p>
        {/* start of the times boxes */}
        <div className="grid mb-5 align-self-start container row" id="times">
          <div className="col-2 d-flex">
            <div className="timeTitle">Prep Time</div>
            <span className="vertical-line"></span>
            <p className="row"> {recipe.prep_time}</p>
          </div>
          <div className="col-2 d-flex">
            <div className="timeTitle">Cook Time</div>
            <span className="vertical-line"></span>
            <p className="row">{recipe.cook_time}</p>
          </div>
          <div className="col-2 d-flex">
            <div className="timeTitle">Total Time</div>
            <span className="vertical-line"></span>
            <p className="row"> {recipe.total_time}</p>
          </div>
          <div className="col-2 d-flex">
            <div className="timeTitle">Servings </div>
            <span className="vertical-line"></span>
            <p className="row">{recipe.servings}</p>
          </div>
          <div className="col-4"></div>
        </div>
      </div>
      {/* This is the section with the image, ingredients and directions */}
      <div className="row mb-5 align-self-start" id="recipeBox">
        <div className="col-4">
          <h2 className="ingredients">Ingredients</h2>
          <ul className="p-0">
            {recipe.ingredients.split(",").map((ingredient) => {
              return (
                <li key={ingredient} className="d-flex p-2">
                  <input
                    type="checkbox"
                    className="align-self-start mt-2 me-2"
                    id="ingredient"
                    value={ingredient}
                    onChange={(e) => actions.ingredientListFunction(ingredient)}
                  ></input>
                  <label htmlFor={ingredient}> {ingredient} </label>
                </li>
              );
            })}
          </ul>
        </div>
        <div className="col-sm-3 col-4 align-self-start">
          <h2 className="directions">Directions</h2>
          <ol className="ol p-0">
            {recipe.directions.split(";").map((direction) => {
              return (
                <li key={direction} className="container pb-3 li">
                  <label htmlFor={direction}> {direction} </label>
                </li>
              );
            })}
          </ol>
        </div>
        <img className="photo col-6" src={recipe.url}></img>
      </div>
    </div>
  );
};
