Project Title: Reminder List

Team Member's Names:
Cole Gaito




Automated Test Cases:

Test Case 1 & 2:
	Use Case Name
		Verify the Validity of a PhoneNumber that is entered into the system.
	Description
		Test the input of a phonenumber to verify its both 10 digits long, and does not contain anything other than numbers.
		Test Case 1 - digits
		Test Case 2 - length of input string
	Pre-conditions
		These tests run independent of the application, and thus there are no preconditions.
	Test steps
		1. Run the application ./list_Input_test.py from the command line.
		2. The automated test cases should ensure that that the functions of the phonenumber tests should validate with either a True or False statement for a valid entry.
		3. You should have a returned message that both tests ran and passed.
	Expected results
		The automated tests should both pass.
	Actual Result
		"Ran 2 tests..."
	Status (Pass/Fail)
		Pass
	Notes
		This is for automated testing.
	Post-conditions
		


Test Case 3:

Test Case 4:

User Acceptance Testing:

Test Case 1:
	Use Case Name
		Verify the "Yes" and "No" respoonses work for the requested initial input.
	Description
		This test will validate that the end user can correctly navigate through the series of Yes/No prior to entering their phonenumber.
	Pre-conditions
		Python3 must be installed.
	Test steps
		1. Run the application ./list_Input.py from the command line.
		2. The user should be greated and prompted to type in a Yes/No answer when responding if a list for them already exists in the program.  The block should appear as below:
		"Hello your list reminder!
		To get started we need to know if you already have a list in our system.
		If you already have a list, type "Yes" if not type "No"."
		3. Type "Yes" or "No".
		4. 
		Upon typing Yes you should receive:
		"To verify you typed: Yes
		You have stated that you have a list of reminders stored. 
		Please enter your phone number so we can retrieve it.
		Please type in your ten digit phone number without any delinations:"

		Upon Typing No you should receive:
		To verify you typed: Yes
		"To verify you typed: No
		You will now to redirected to create a new reminder list.  
		Please enter a phonenumber to be associated with your acount:
		Please type in your ten digit phone number:" 
	Expected results
		Upon typing "Yes" or "No" you should receive a prompt requesting for a phone number.
	Actual Result
		Was prompted with the correct result.
	Status (Pass/Fail)
		Pass
	Notes
		This is for manuel user testing.
	Post-conditions

Test Case 2:
	Use Case Name
		Verify the input other than "Yes" and "No" respoonses prompt user for the requested initial input.
	Description
		This test will validate that the end user can only type "Yes" or "No" case-sensitive into the system.
	Pre-conditions
		Python3 must be installed.
	Test steps
		1. Run the application ./list_Input.py from the command line.
		2. The user should be greated and prompted to type in a Yes/No answer when responding if a list for them already exists in the program.  The block should appear as below:
		"Hello your list reminder!
		To get started we need to know if you already have a list in our system.
		If you already have a list, type "Yes" if not type "No"."
		3. Type something other than "Yes" or "No" including "yes" or "no".
		4. You should have a response of:
		"To verify you typed: <what was typed in Step 3>
		Your inputs did not match either of the acceptable responsese.  You have three attempts before the program closes.  Please try again.
		Please type your response here:"
		5. Type something other than "Yes" or "No" without quotes two more times prior to quitting.
	Expected results
		Upon failing to receive the proper input you should be returned to the command line after 3rd attempt.
	Actual Result
		Was returned to command line.
	Status (Pass/Fail)
		Pass
	Notes
		This is for manuel user testing.
	Post-conditions

Test Case 3:

Test Case 4:


