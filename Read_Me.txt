This Txt File is the instructions for the various programs in the 
Staubjr/Project Repository:
	
1.) Biodiversity_Semester_Project_Environmental_Stochasticity_with_Genetics_V1.py
2.) Code_to Read Environmental_and_Demogrpahic_Stochasticity.py

I also am including text files for the data that I got when I ran the 
simulation. Given the random nature of the model this may vary; however,
it should not vary by much. Also, note that I am using a trial size of
100 due to limits in computational efficiency. If one has more efficient
machines or just more computational time available you can run it for more
trials. I think that you will see diminishing marginal returns passed my 
chosen trial size.

The order to run the code in is the simulation, then read and plot. For the 
simulation code (1) you can run it for the environmental and demographic
stochasticity in the same way. Note, that I commented out the demographic
stochasticity methods, but all you need to do is 'uncomment' this and then run
it instead of the environmental stochasticity method.

**** WARNING: BE CAUTIOUS OF HOW YOU WRITE TO TEXT FILES AS THIS MAY RESULT IN
 	      ERRORS IN READING THE TEXT FILE WITH MY CODE (2).  YOU MAY NEED 
              TO AMMEND THE CODE SLIGHTLY ****

Once you read the data and then create your figure using code (2), note that it
should have linear regression models with the correct correlation coefficient 
models plotted. I promise there are just a few more things to note.

1.) The error bars are plus and minus one standard error.
2.) The demogrpahic stochasticity data does not look really good when you 
    plot all of the points, so I elected to plot only half of them. I think
    this is the reasonable choice here, but just note that the error bars
    use the full 100 data points, NOT THE PLOTTED 50 DATA POINTS.

Thank you for reading the initial documentation.

I am leaving the program open source for others to hopefully ammend, utilize,
or just make better. The model currently uses the following assumptions,
which could be changed based on your uses and applications:

ASSUMPTIONS: (You know what they say when you assume things...)

1.) Closed population (no gene flow or mutations)
2.) K = 2000 individuals
3.) Individuals mature in one generation and can mate with parents
4.) Monogamous, annual breeding system
5.) Demographic stochasticity is modeled through penguin pairs producing a 
    random number of offspring (0-3) each year 

For any inquiries on how to ammend the code, questions, or comments about
making this program better/more efficient please contact me.

Email: JacobStaub99@gmail.com

Last Update: 11/25/2019

