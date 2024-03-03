cd "Coding_Final_Assignment"
pwd


/* importing csv file, with 1 row as variable name */
*Reading .csv data in in Stata
import delimited Data_qualtrics_edited.csv, clear varnames(1)

/*dropping rows that only contained the questions and no data, furthermore, one observation didn't finish the suvery, so that was also dropped.*/
drop in 1/67
drop if finished == "0" 


/*dropping rows that arent relevant*/
		drop startdate enddate status ipaddress progress durationinseconds finished recordeddate recipientlastname recipientfirstname recipientemail externalreference locationlatitude locationlongitude distributionchannel userlanguage thankyou_firstclick thankyou_lastclick thankyou_pagesubmit thankyou_clickcount

/*Fixing common data quality errors: destring data, converting string to numbers (where possible) and replacing with number*/
		destring, replace

* Removing "_1" suffix from variable names, as for some reason that is added after importing
foreach var of varlist leftq1_1 - rightq30sc_1 {
    local newvar : subinstr local var "_1" "", all
    rename `var' `newvar'
}

*Fixing common data quality errors: string vs number, missing value.

*saving cleaned dta 
save clean.dta, replace