{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ad0d46a-780d-4713-91e4-a2db84435347",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (766953840.py, line 15)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[1], line 15\u001b[1;36m\u001b[0m\n\u001b[1;33m    num_feat = st.selectbox(\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "import seaborn as sns\n",
    "df = sns.load_dataset('titanic')\n",
    "st.title('Titanic Dashboard')\n",
    "st.subheader('Dataset')\n",
    "st.dataframe(df)\n",
    "st.subheader('Data Numerical Statistic')\n",
    "st.dataframe(df.describe())\n",
    "st.subheader('Data Visualization with respect to Survived')\n",
    "left_column, right_column = st.columns(2)\n",
    "with left_column:\n",
    "   'Numerical Plot'\n",
    "    num_feat = st.selectbox(\n",
    "   'Select Numerical Feature', df.select_dtypes('number').columns)\n",
    "    fig = px.histogram(df, x = num_feat, color = 'survived')\n",
    "    st.plotly_chart(fig, use_container_width=True)\n",
    "with right_column:\n",
    "   'Categorical column'\n",
    "    cat_feat = st.selectbox(\n",
    "    'Select Categorical Feature', df.select_dtypes(exclude =   'number').columns)\n",
    "    fig = px.histogram(df, x =cat_feat, color = 'survived' )\n",
    "st.plotly_chart(fig, use_container_width=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
