import React from "react";
import { useState } from "react";
import "../../styles/form.css"
export  const FormPage = () => {
  const [title, setTitle] = useState('')

  function onsubmit() {
    
  };
    return(
      <div class="container form mt-5">
          <div className="h1-container">
          <h1 class="heading">Submit your recipe to Foodgasm</h1>
          </div>
          <div class=" container mt 8">
          
            <form class="row g-8 mb-100" />

            <div class="rtitle">
              <label for="rtitle">Recipe Title:</label>
              <input  value={title} onChange={(e) => setTitle(e.target.value)} class="form-control input-sm" id="rtitle" type="text" />
            </div>

            <div class="nos">
              <label for="servings">Number of Servings:</label>
              <input class="form-control input-sm" id="servings" type="text" />
            </div>

            <div class="ing">
              <label for="ingre">Ingredients:</label>
              <textarea class="form-control input-sm" id="ingre" rows="3" type="textarea" />
            </div>

            <div class="direct">
              <label for="directions">Directions:</label>
              <textarea class="form-control input-sm" id="directions" rows="3" type="textarea" />
            </div>

            <div class="preptime">
              <label for="preptime">Prep Time:</label>
              <input class="form-control input-sm" id="preptime" type="text" />
            </div>

            <div class="cooktime">
              <label for="cooktime">Cook time:</label>
              <input class="form-control input-sm" id="cooktime" type="text" />
            </div>

            <div class="totaltime">
              <label for="totaltime">Total Time:</label>
              <input class="form-control input-sm" id="totaltime" type="text" />
            </div>

            <div class="credit">
              <label for="credit">Credit:</label>
              <input class="form-control input-sm" id="credit" type="text" />
            </div>

            <div>
            <form className="mt-2">

              <label for="menu type">Meal Type:</label>
              <select name="mealtype" id="mealtype">
                <option value="breakfast">Breakfast</option>
                <option value="lunch">Lunch</option>
                <option value="dinner">Dinner</option>
                <option value="dessert">Desserts</option>
                <option value="snacks">Snacks</option>
                <option value="drinks">Drinks</option>

               </select>
              </form>


          </div>


            <label class="customFile" for="customFile">Submit Photo Here</label>
            <input type="file" class="form-control  btn my-3" id="customFile" />
            <div>
            <button onClick={onsubmit}className="btn my-3">Submit</button>
            </div>


            <form />
          </div>
      


     </div>
    );
};

