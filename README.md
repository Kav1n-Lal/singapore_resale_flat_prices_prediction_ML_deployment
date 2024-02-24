# singapore_resale_flat_prices_prediction_ML_deployment
### App Deployment link:
-  I used the **app.py** to create a **Streamlit** app and deployed live using **Streamlit Cloud**.-->>[(https://singaporeresaleflatpricespredictionmldeployment-erzeps7hqradto.streamlit.app/)]
- - - ## Regression R2 and RMSE score Table
|    Model             |  Train(R2-score)   |  Train(RMSE)      | Test(R2-score)     |  Test(RMSE)       |
| :------------------- | -----------------  |-----------------: | -----------------  |-----------------: |
| Linear Regression    |      0.7943         |0.0494              | 0.7943              |0.0494              |
|HistGradientBoostingRegressor|0.9615        |0.0213              | 0.9608              |0.0215              |

- ### Project Demonstration video link:
- Entire project explanation-[https://drive.google.com/file/d/1fokFKIVkc-_o1cI3FjBFH5SriEuzdXCq/view?usp=sharing]
### Others:
- View **flat_resale_price_ML.ipynb** -where I have done data cleaning, preprocessing and training of various regression models and feature selection.
- View **singapore_pickling.ipynb** -the refined notebook where I have used only the *selected 3 features*  and used the **HistGradientBoostingRegressor** model to run the entire dataset and save the model as a pickle file named **singapore_resale_price_saved_steps_regressor.pkl**.
- Totally there were **10 independent features**, but I created a ML model model with **just 3 independent features** with good R2 and RMSE values as tabulated above.
