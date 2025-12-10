try:
    import os
    import streamlit as st
    import pandas as pd
    from replace_image_text import image_to_text
    from excel_date import date_conversion
    from highlight import hihglight
    from remove import remove
    from datetime import datetime


    def highlight_failed_rows(row):
        if any('Failed' in str(val) for val in row):
            return ['background-color: #ff4444; color: white'] * len(row)
        return [''] * len(row)

    try:
        uploaded_file = st.file_uploader("Upload the file", type="xlsx")

        if uploaded_file:
            dest = os.path.join(os.getcwd(), "Excel_files", "temp.xlsx")
            pd.read_excel(uploaded_file).to_excel(dest, index=False)
            df=pd.read_excel(dest)
            image_to_text(uploaded_file,dest)
            date_conversion(dest,dest)
            df = pd.read_excel(dest)
            #st.table(df)
            styled_df = df.style.apply(highlight_failed_rows, axis=1)
            st.table(styled_df)
            hihglight(dest, dest)
            remove(dest)
            now = datetime.now()
            filename="Process_chain_"+now.strftime("%d_%b_%y")+"_final.xlsx"
            with open(dest, "rb") as template_file:
                template_byte = template_file.read()

            st.download_button(label="Click to Download Template File",
                           data=template_byte,
                           file_name=filename,
                           mime='application/octet-stream')
            os.remove(os.path.join(os.getcwd(),"Excel_files","temp.xlsx"))




    except Exception as e:
        st.error(e)
except Exception as e:
    st.error(e)










