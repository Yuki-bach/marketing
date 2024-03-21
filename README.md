## DAT494 - Capstone Project
- Customer Segmentation
- Dataset: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## EDA Dashboard
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dat490-marketing.streamlit.app/)

## How to Run Streamlit in Local Environment
```
1. Install streamlit
$ pip install streamlit

2. run streamlit
$ streamlit run app/main.py
```

## Datasets folder
- `eda.ipynb` - Our first EDA notebook (it's not used now)
- `feature_engineering.ipynb` - Create new features, and save in datasets/df_train.csv
- `methodology_kmeans.ipynb` - for methodology submission assignment
- `methodology_dbscan.ipynb` - for methodology submission assignment
- `rfm_analysis.ipynb` - Create clusters for each RFM columns, and then create the overall score

## Git Cheat Sheet for Team Collaboration

```
1. Update your local repository with the latest changes from the remote:
$ git switch main
$ git pull

2. Create a new branch and switch to it:
$ git switch -c your-branch-name

3. Make some changes to code

4. Stage all changes for commit:
$ git add -A

5. Commit your changes with a descriptive message:
$ git commit -m "what you did and/or why you did"

6. Push your branch to the remote repository:
$ git push --set-upstream origin your-branch-name

7. Go to the github "Pull Request" page, and create the Pull Request

As for the 4 and 5, you can also do this using vscode.
```
