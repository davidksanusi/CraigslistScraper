import gspread

# THIS WILL BE OUR DATABASE FOR SMALL-SCALE TESTING
# WE COULD WORK WITH A LOCAL CSV LIBRARY and EXCEL BUT GOOGLE SHEETS ALLOWS US TO ACCESS OUR DATA ONLINE
# IF YOU PREFER TO WORK WITH A LIBRARY LIKE PANDAS, THEN FEEL FREE TO REPLACE THE BELOW CODE

# PLEASE SEE THE GSPREAD DOCUMENTATION LIBRARY TO LEARN HOW TO CONNECT TO GOOGLE SHEETS
gc = gspread.service_account(filename="/Users/David/PycharmProjects/yp-scraper/creds.json")
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1m3S0MgCRZxXp1aG-em2Fzovnf1hABfJ4BGrY3p95p0s/edit#gid=105903045').get_worksheet(0)
sh2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1m3S0MgCRZxXp1aG-em2Fzovnf1hABfJ4BGrY3p95p0s/edit#gid=105903045').get_worksheet(1)
