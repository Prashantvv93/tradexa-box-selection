# AI Usage

## 1. Which AI tool did I use?

I used ChatGPT to help me understand the assignment, write some code, fix errors, and test my project.

## 2. What did I ask ChatGPT?

I asked ChatGPT for help with these things:

- Understanding what the project needs to do.
- Choosing the right technology for the project.
- Creating the Django project and connecting the files.
- Writing the logic to find a suitable shipping box.
- Creating an API to send product details and get the recommended box.
- Checking product dimensions and weight.
- Writing test cases and fixing errors.
- Understanding how to run and test the project.

## 3. What suggestions did I use?

I used suggestions that helped me build the project, such as:

- Using Django and Django REST Framework.
- Creating a model to store shipping box details.
- Checking whether a product fits inside a box.
- Selecting the cheapest box that can safely fit the product.
- Validating the input before processing it.
- Writing tests to check whether the code works correctly.

I also changed some code and followed the steps to understand how the different files work together.

## 4. What suggestions did I change or not use?

I did not use every suggestion without checking it.

I reviewed the code and made changes when needed. For example, I fixed a warning in the input validation code and added a test to check what happens when two suitable boxes have the same price.

I focused on keeping the project simple and easy to understand.

## 5. What mistakes did AI make?

During development, I received a warning related to input validation. I checked the warning and updated the code to fix it.

I also checked the API response and test results instead of assuming that the code was correct just because it was generated.

## 6. How did I check the project?

I used the following command to run the tests:

python manage.py test boxes

The initial five tests passed successfully after fixing the validation warning.

I also tested the API by sending product dimensions and weight through PowerShell. The API returned the recommended shipping box.

I will run the complete test suite again before submitting the final project and update the test results with the actual output.

## 7. Decisions I made

I made the following decisions for the project:

- Product dimensions can be rotated to fit the box.
- Dimensions are measured in centimetres.
- Weight is measured in kilograms.
- The system selects the cheapest suitable box.
- If two suitable boxes have the same price, the smaller-volume box is selected.
- If no box can fit the product, the API returns a message saying that no suitable box was found.

## 8. Final note

I used ChatGPT as a helper during development. I also ran the project, checked the API response, and tested the code to understand how the system works.

The final code and test results should be checked before submission.
