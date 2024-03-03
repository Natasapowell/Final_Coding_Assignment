*using previouslz created clean dataset that was saved in STATA
use clean.dta

/*generating binary variable for left treatment*/
	gen left = leftq1 <=111 

/*creating a loop to generate the cumulative variables and to recode scale option for each question*/
forval  i = 1/30 {
	egen q`i' = rowtotal(leftq`i' leftq`i'sc rightq`i' rightq`i'sc)
		replace q`i' = leftq`i'sc if left == 1  & q`i' > 100
		replace q`i' = rightq`i'sc if left == 0 & q`i' > 100	
}

* running regressions and saving coefficients as Q`i', for all 30 questions
forval  i = 1/30 {
	reg q`i' left
	estimates store Q`i'
} 

*graphing the resulting coefficients
coefplot Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10 Q11 Q12 Q13 Q14 Q15 Q16 Q17 Q18 Q19 Q20 Q21 Q22 Q23 Q24 Q25 Q26 Q27 Q28 Q29 Q30, drop(left) vertical
*saving graph and exporting as jpg
graph export "C:\Users\Powell_Natasa\Desktop\Coding_Final_Assignment\coefplotgraph.jpg", as(jpg) 

*creating another graph
hist q1
*saving graph and exporting as jpg
graph export "C:\Users\Powell_Natasa\Desktop\Coding_Final_Assignment\Graph.jpg", as(jpg) 
