import streamlit as st  
import pandas as pd
import pickle

def main():
    html_temp = """
    <div style="background:#025287 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Singapore  Resale Flat Prices Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write("""### We need some information to predict the resale price""")
    
    

    z=pd.read_csv('singapore_features.csv')
    #z['year']=[str(i) for i in list(z['year'])]
    
    # Storing all user input 
    input_dict={ 'street_name':'', 'year':'2023', 'floor_area_sqm':''}

    form = st.form("form1")

    street_name=form.selectbox('Choose street_name',list(z['street_name'].unique()))
    input_dict['street_name']=street_name

    floor_area_sqm=form.selectbox('Choose floor_area_sqm',list(z['floor_area_sqm'].unique()))
    input_dict['floor_area_sqm']=floor_area_sqm
    
    #year=form.selectbox('Choose flat activation year',list(z['year'].unique()))
    #input_dict['year']=year

    ok=form.form_submit_button("PREDICT") # 
    safe_html ="""  
        <div style="background-color:#B3CBDB; padding:10px >
        <h2 style="color:white;text-align:center;"> Result</h2>
        </div>
        """  
    if ok:
        
        def load_model():
            with open('singapore_resale_price_saved_steps_regressor.pkl','rb') as file:
                data=pickle.load(file)
            return data

        data=load_model()

        resale_box_cox_transform=data['transformer1_resale_price']
        mean_encoder=data['mean_enc']
        scaler=data['scaler']
        regressor_loaded=data['model']
        
        A=pd.DataFrame(input_dict,index=[1])
        
        B=mean_encoder.transform(A[['street_name', 'year','floor_area_sqm']])
        
        C=scaler.transform(B)
        
        y_pred=regressor_loaded.predict(C.reshape(1,-1))
        t=resale_box_cox_transform.inverse_transform(y_pred.reshape(-1,1))
       
        u=str(round((list(t)[0][0]),2))+'/-'
        st.success(f'### Predicted Flat Resale Price is : {u}')
        
        if t[0][0]>100:
            st.markdown(safe_html,unsafe_allow_html=True)
        
        st.markdown(f':green[Take a look at the average flat resale price over the years at] :blue[{street_name}] :green[area]')
       
        visual_df=z.loc[(z['street_name']==street_name) & (z['floor_area_sqm']==floor_area_sqm)]
        g=visual_df.groupby('year')['resale_price'].mean()
        st.bar_chart(g)
        
        

if __name__=='__main__':
        main()