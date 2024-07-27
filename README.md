# ish Project Manager Back-end

This is the back-end REST API for the ish Project manager, full project details can be found in the front-end app repo. This README file contains backend specific information only.

The REST API is built with Django using the Django Rest Framework Library and uses PostgreSQL as the database. This stack ensures a highly flexible and robust API framework for efficiency and scalabilty.

The backend architecture follows a minimalist and efficient approach, primarily utilizing the built-in default views provided by DRF to manage all CRUD (Create, Read, Update, Delete) operations. This ensures that the codebase remains clean and maintainable while still providing all the necessary functionality for interacting with the application's data.

Authentication is a critical aspect of any application, and for this, I have implemented JSON Web Token (JWT) authentication. JWT is a compact, URL-safe means of representing claims to be transferred between two parties. It is widely used for securely transmitting information between parties as a JSON object. In the application, JWT handles user authentication and session management, ensuring that only authorized users can access and modify data.

To further enhance security, we have customized the permission classes in DRF. These custom permission classes allow the definition fine-grained access control policies, ensuring that users can only perform actions that they are authorized to do. This adds an additional layer of security and ensures that our application adheres to the principle of least privilege.

Overall, the backend is designed to be robust, secure, and efficient, providing a solid foundation for the application's functionality while maintaining simplicity and ease of maintenance.

## Permissions and Access Control

The permission system for the application is designed to ensure that only authorized users can access and modify data. When a user logs in, they receive an access token, which must be included in every subsequent API request. These tokens are then decoded to identify the user making the request.

CRUD (Create, Read, Update, Delete) operations are restricted based on the parent project associated with the data being accessed or modified. All epic, sprint, and item models are linked to a project object, which in turn has an owner. Whenever one of these models is accessed or modified, the application checks the parent project and verifies that the user attempting the operation is the owner of the project. If the user is not the owner, the operation is denied, and an error is returned.

This permission system ensures that only users who own a project can view or edit data within that project, maintaining data integrity and security.

## Deployment

This is the deployment process for the back-end, for full deployment details including front-end and how to connect the application layers please refer to the documentation in the front-end repo.

Currently both front end and backend are deployed as Docker containers running on Coolify, a self-hosted Vercel like platform for a seamless and easy to use CI/CD process.

Here are the deployment steps

### Setting Up Coolify

Setting up Coolify on a compatible Linux instance is a straightforward process that can be accomplished by running their installation script from the terminal. Detailed instructions and the installation script can be found on the Coolify website: https://coolify.io/self-hosted.

1. **Prepare Your Linux Instance**:
   Ensure that your Linux instance meets the compatibility requirements specified by Coolify. This typically involves having a recent version of a Linux distribution and ensuring that your system is up-to-date.

2. **Run the Installation Script**:
   Open your terminal and execute the installation script provided by Coolify. This script will handle the download and installation of all necessary components. You can find the script and detailed instructions on the Coolify website.

   ```sh
   curl -fsSL https://get.coolify.io | bash
   ```

3. **Access Coolify Dashboard**:
   Once the installation is complete, Coolify will be accessible on port 8000 of your server. Open your web browser and navigate to `http://your-server-ip:8000`. You will be prompted to log in or create an administrator account. Follow the on-screen instructions to set up your admin credentials.

4. **Create a Project and Environment**:
   After logging in, you will be directed to the Coolify dashboard. Here, you can create a new project and set up an environment for your application. This involves specifying the necessary resources such as the front-end, back-end, and database.

   - **Create a Project**: Click on the "Create Project" button and provide a name and description for your project.
   - **Set Up Environment**: Within your project, create an environment (e.g., development, staging, production). This is where we will deploy the necessary resources in the next steps.

5. **Deploy Your Application**:
   With your project and environment set up, you can now deploy your application.

By following these steps, you can leverage Coolify to streamline the deployment and management of your applications, ensuring a seamless and efficient CI/CD process.

### Deploying the Database

Coolify supports multiple resource types, including PostgreSQL, which we will use as our database.

1. **Add New Resource**:
   Click the "Add Resource" button and select PostgreSQL from the Databases section.

2. **Configure Installation**:
   Most configuration settings can be left as defaults. However, if you plan to use this database for development purposes and need to connect to it from your local machine or if you are deploying the front-end on another server, you may want to make it publicly available. To do this, select the "Make it publicly available" checkbox and optionally change the public port.

   Making the database publicly available is often necessary to push database migrations from your development environment to the production database.

3. **Start The Database**:
   Once the configuration is complete, click the "Start" button to start the database. Copy the database URL as it will be needed in the next steps.

4. **Apply Migrations**:
   In your development environment, apply all migrations to the database. Copy the database URL and set it as your database URL in your environment file. Once the database is connected, run `python3 manage.py migrate` to apply the migrations to the new database.

### Deploy the Back-End

Coolify uses Nixpacks to automatically build and deploy Docker images. This approach works well for the back-end without requiring customization.

1. **Add New Resource**:
   Click the "Add Resource" button and select "Public Git Repository" from the options. Copy and paste the GitHub repository link, including the branch, into the Git repo link field. Leave the build pack option as the default Nixpacks, which will detect all configurations and create the Docker image automatically without needing a Dockerfile. The default port can remain at 3000.

2. **Configure Installation**:
   Most configuration settings are optional. You may want to customize fields such as the name, description, and domain. Focus on the essential configuration by setting the environment variables. Add three environment variables: "DATABASE_URL" (the URL created when deploying the database), "JWT_SECRET_KEY" (a strong random secret key for JWT token generation), and "SECRET_KEY" (used by Django).

3. **Deploy The Backend**:
   Once the configuration is complete, click the "Deploy" button to deploy the application. Copy the public URL for this service as it will be needed when deploying the front end.

## Testing

### Validator Testing

### API Testing

The raw API functionality is tested using POST Man by making API requests to all endpoints to ensure data validatity and application security.

As the front-end application limits the types of API requests that are made it is essential to test the back-end manually by making unintented API requests with invalid/unintended request methods, body data and access tokens to ensure the backend behaves appropriately by throwing errors and not letting unauthorized API requests peform any operation on the database.

This is the testing process for every API endpoint:

#### Register

1. **Objective**: Verify that users can successfully sign up with valid data.
2. **Steps**:
   1. Make a request to the registration endpoint with valid sign up details.
   2. Observe the repsonse.
   3. Repeat with invalid data
3. **Expected Results**:
   1. When a request is made with valid details a success response is received and the new account is registered in the database.
   2. When a request is made with invalid details an error response is received and the new account is not registered in the database

#### Login

1. **Objective**: Verify that users can successfully login with valid data.
2. **Steps**:
   1. Make a request to the token enpoint with valid login credentials
   2. Observe the repsonse.
   3. Repeat with invalid data
3. **Expected Results**:
   1. When a request is made with valid details a success response and a pair of access and refresh tokens are received
   2. When a request is made with invalid details an error response is received and no access tokens are received.

#### All Other Endpoints

The testing process for all other end points are the same testing CRUD functionality on all models that are considered children of projects. Each step makes one criteria of the request data invalid ensuring each criteria and checked and dealt with appropriately.

1. **Objective**: Verify that all project child data can only be accessed and modified by project owners using the intended request method with valid data.
2. **Steps**:
   1. Make a request to endpoint using valid request tokens that match the project owner, with a valid request method and valid data.
   2. Observe the repsonse.
   3. Make a request to endpoint using valid request tokens that match the project owner, with a valid request method but invalid data.
   4. Observe the response.
   5. Make a request to endpoint using valid request tokens that match the project owner with valid data but an invalid request method.
   6. Observe the results.
   7. Make a request to endpoint using using a valid request method and valid data but with valid tokens of another user.
   8. Observe the results.
   9. Make a request to endpoint using using a valid request method and valid data but with invalid tokens.
3. **Expected Results**:
   1. Step 1 should return a success reponse and valid data.
   2. Step 3 should return a bad request response, all data should be unaffected.
   3. Step 5 should return a request method not allowed response, all data should be unafected.
   4. Step 7 should return an unauthorized operation permission error, all data should be unafected.
   5. Step 9 should return an unauthorized operation permission error, all data should be unafected.
