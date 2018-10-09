# Microsoft Custom Vision and Azure Notebooks - Deep Learning: using Fashion MNIST Dataset

> “I need to sort out my wardrobe” 

*Image classification of fashion items using Deep Learning* - Classifying numbers and letters is so last season .. Let’s classify our wardrobes instead! Learn all about the in’s and out’s of image classification using deep learning. 

### Contents:
* [Pre-requisities](https://github.com/amynic/deep-learning-fashion#pre-requisities)
* [Microsoft Custom Vision for Image Classification](https://github.com/amynic/deep-learning-fashion#microsoft-custom-vision-and-azure-notebooks-for-image-classification)
* [Azure Notebooks for Image Classification](https://github.com/amynic/deep-learning-fashion#azure-notebooks-for-image-classification)
* [Microsoft Data Science Virtual Machine for Deep Learning](https://github.com/amynic/deep-learning-fashion#microsoft-data-science-virtual-machine-for-deep-learning)



In this 2 hour workshop we will offer two forms of image classification using deep learning. One will be using the Microsoft Custom Vision service and transfer learning, and the other will be using the Microsoft Azure Notebooks and the deep learning API, Keras. 

Both exercises will show you, step-by-step, how to classify clothing into categories such as dresses, t-shirts, sandals, trainers etc. The dataset we will use will be the Fashion MNIST dataset from Zalando the online fashion brand: https://github.com/zalandoresearch/fashion-mnist 

## Pre-requisities

* Bring your laptop
* Have access to a modern web browser (Microsoft Edge, Google Chrome, Firefox etc)
* Have access to a Microsoft account (outlook.com, Hotmail.com etc) or sign up here: http://signup.live.com/ 
* Experience with coding, we will be using the Python Language

## Microsoft Custom Vision for Image Classification

1. Download and unzip the 'dataset.zip' file from GitHub *(should take around 10 secs)*. 
    * Select the dataset folder and choose the download button
    ![download data](./images/download.JPG "download data")
    * Or download the whole repository from the Readme page
    ![download folder](./images/downloadfolder.JPG "download folder")
    * This contains two folders: train and test data. Look in the folder and view the images
    ![Training Images](./images/images.JPG "Training Images")
2. Visit [www.customvision.ai](http://www.customvision.ai/) and click 'Sign In'
    * Enter your Microsoft Account email and password
    * accept the permissions ask window
    ![permissions](./images/permissions.JPG "permissions")
    * Continue with the trial account
    ![trial account](./images/trialmode.JPG "trial account")
    * now you should see a portal like below
    ![portal](./images/portal.JPG "portal")

3. Create a new project
    * Select new project and complete the fields as shown below
    ![Create new project](./images/createnewproject.JPG "Create new project")
        * Name: name of project
        * Description: description of project
        * Project Types: Classification
        * Classification Types: Multiclass (single tag per image)
        * Domains: Retail
    * Finally click create project and you should see the below
    ![Get Started](./images/getstarted.JPG "Get Started")
 
4. Now lets add training images and classes to our model
    * Click Add Images in the top left
    ![Add Images](./images/addimages.JPG "Add Images")
    * From the 'train' folder of images, every image is prefixed with a label number. For example: 0label_image1.png - this means label/class/category 0 and image 1. There are 0-9 classes for this model and 25 training images per class. Select all the images for class 0 and choose open
    ![Select Images](./images/selectimages.JPG "Select Images")
    * On the upload screen, review the images and in the 'My Tags' box type 'tshirt' and hit enter.
    * Once the 'tshirt' tag turns blue, select 'upload 25 files'
    ![Upload](./images/upload.JPG "Upload")
    * Now you should see your images added to the environment for one class which is labelled on the left
    ![One Class Added](./images/oneclassadded.JPG "One Class Added")

5. Now complete Step 4 for the other 9 classes. Find below the corresponding label number to label text:

| Label Number      | Label Text  |
| ------------- |:-------------:|
| 0      | tshirt |
| 1      | trouser |
| 2      | jumper |
| 3      | dress |
| 4      | coat |
| 5      | sandal |
| 6      | shirt |
| 7      | trainers |
| 8      | bag |
| 9      | boots |


* Select images from each category to upload
* Add the correct tag to each class
* Complete this for classes 0-9
![All Classes Added](./images/allclasses.JPG "All Classes Added")

6. Once all images are uploaded you are ready to train the model. In the top right corner click 'Train'
![train](./images/train.JPG "train")

7. After training you will be take to the 'Performance' tab where you will see summary statistics of the trained model you created - its not too bad!
![performance](./images/performance.JPG "performance")
    * You can also review the performance metrics by category
    ![performance by category](./images/perfbycategory.JPG "performance by category")

8. Now to test the model on new images
    * We can test the model quickly in the UI.
    * In the top right click 'Quick Test'
    ![quick test](./images/quicktest.JPG "quick test")
    * choose browse for files and select an image from the 'test' folder. Click open and view the models evaluation of this image.
    ![test](./images/test.JPG "test")
    


These images are 28 x 28 pixel images and so are very small. Therefore we will try another way of testing the model using an Azure Notebook.

Notebook editors are often using in Machine Learning.

## Azure Notebooks for Image Classification

1. Browse to [https://notebooks.azure.com/](https://notebooks.azure.com/)
    * Choose sign in
    ![Azure notebooks sign in](./images/azurenotebooks.JPG "Azure notebooks sign in")
    * Sign in with your Microsoft Account username and password
    ![Permissions](./images/permision2.JPG "Permissions")
    * Create a user ID - such as your name
    ![Create User ID](./images/userid.JPG "Create User ID")

2. Now you are signed in lets start running some code
    * Create a new library. Click create library
    ![Create Library](./images/createalibrary.JPG "Create Library")
    * Now select new to upload a notebook
    ![Upload Notebook](./images/notebooks.JPG "Upload Notebook")
    * Choose 'From Computer' and 'Choose Files' - then locate the custom-vision-sample.ipynb file from path: \deep-learning-fashion\custom-vision
    ![Upload Notebook](./images/uploadnotebook.JPG "Upload Notebook")
    * Choose the uploaded python notebook file to open it
    ![File Uploaded](./images/file.JPG "File Uploaded")
    * You may recieve a message about the notebook Kernel. If so please select Python 2 and select 'Set Kernel'
    ![Select Kernel](./images/selectkernel.JPG "Select Kernel")

3. To run code in a python notebook. You select the code cell and press 'CTRL' + ENTER on your keyboard. You will see a small asteriks (*) at the left side of the notebook stating the notebook is running. Once complete the output of the code will be printed below each cell.
![Code](./images/code.JPG "Code")
    * To learn more about Jupyter Notebooks review the documentation here: [https://jupyter-notebook.readthedocs.io/en/stable/notebook.html](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)

4. There are a few keys and urls we need to edit before running the code:
    * **customvisionapi_key** - you can find your 'prediction key' in customvision.ai UI under settings
    *Settings Tab
    ![Settings](./images/settings.JPG "Settings")
    * Key
    ![Keys](./images/keys.JPG "Keys")
    * **custom_vision_url** - you can find this information under 'Performance' tab, choose 'Prediction URL' button and copy everything after *https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/* from the 'If you have an image URL' section

    ![Prediction Endpoint](./images/predictionendpoint.JPG "Predicition Endpoint")

5. Now run the code using CTRL + ENTER and review the output. Which class was predicted with the highest probability?
![output](./images/output.JPG "output")

6. Why not try another image to test? Select another image from the 'test' folder: [https://github.com/amynic/deep-learning-fashion/tree/master/dataset/test](https://github.com/amynic/deep-learning-fashion/tree/master/dataset/test) and replace the filename in the **body** variable


# [OPTIONAL] Microsoft Data Science Virtual Machine for Deep Learning

1. Sign into Microsoft Azure: [http://azure.microsoft.com/](http://azure.microsoft.com/) and click 'Portal' in the top right corner

2. Lets create a Data Science Virtual Machine (DSVM) (Linux Ubuntu). This is a great data science tool as it is a preconfigured virtual machine image with all the data science packages and software already installed. To find out more about the DSVM check out the documentation here: [https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview)
    * In the Azure Portal, click 'Create a resource' in the top left corner
    * Search for 'data science' and select 'Data Science Virtual Machine for Linux (Ubuntu)'
    ![DSVM](./images/dsvm.JPG "DSVM")
    * Choose create and fill in the fields to create a Virtual Machine image
    ![Create DSVM](./images/createdsvm.JPG " Create DSVM")
        * **Subscription:** choose your subscription
        * **Resource Group:** select 'Create new' and call it 'techknow'
        * **Virtual machine name:** choose a name for your machine such as 'techknow-<yourname>'
        * **Region:** North Europe
        * **Availability options:** no infrastructure redundancy required
        * **Image:** keep default
        * **Size:** keep default
        * **Authentication type:** password
        * **username:** create a log in username, for example your name or alias
        * **password:** enter a string password and remember this you will need to use it shortly
    * Click Review + create button
    ![Review DSVM](./images/review.JPG " Review DSVM")
    *The DSVM will start to deploy and you get a visual progress check on the items being created in your Azure Subscription
    ![Review progress](./images/deploymentinprogress.JPG " Review progress")
    * Once created choose 'Go to resource' and open the VM page
    ![VM](./images/vm.JPG "VM")

3. Connect to your Data Science Virtual Machine (DSVM)
    * On the VM page click connect to find the IP address of the VM and copy it
    ![Connect IP](./images/connect.JPG "Connect IP")
    * Open a modern web browser and type: https://<ipadresshere>:8000/ to connect to Jupyter Hub to run a notebook
    * You will recieve a certificate error. Choose the link 'Details' and click 'Go on to the webpage'
    ![Connect cert](./images/secure.JPG "Connect Certificate")
    * Login to Jupyter Hub using the Username and Password you setup for your virtual machine
    ![Login Screen](./images/login.JPG "Login Screen")
    * Once logged in you will see the Jupyter Notebook folder structure with many sample files already prepopulated.
    ![Jupyter](./images/dsvmjupyter.JPG "Jupyter")

4. Create a new folder for your code files
    * Choose 'New' and select 'Folder'
    ![folder](./images/newfolder.JPG "folder")
    * Rename the folder by locating the directory and clicking rename.
    ![rename](./images/rename.JPG "rename")
    * Rename the folder to: 'fashion-deep-learning'
    ![rename](./images/folderrename.JPG "rename") 
    * Upload the file 'Fashion_MNIST_Deep_Learning-code.ipynb' from [https://github.com/amynic/deep-learning-fashion/blob/master/deep-learning/Fashion_MNIST_Deep_Learning-code.ipynb](https://github.com/amynic/deep-learning-fashion/blob/master/deep-learning/Fashion_MNIST_Deep_Learning-code.ipynb)
    ![upload](./images/uploadpy.JPG "upload")
    * Once uploaded click the file to open it

5. Explore and run the Jupyter Notebook
    * Once in the notebook you can run each cell by pressing CTRL + ENTER or you can select Cell from the toolbar and run all the cells at once
    * Read through the comments in the notebook to understand the code further and run till completion

6. Edit the Jupyter Notebook to edit the model
    * Now can you edit the code in places to make changes to your model? Look out for hints, tips and questions in the notebook for how to edit the model

![Deep learning code](./images/deeplearningcode.JPG "Deep Learning Code")


# Remember to delete your resources

The custom vision service and Azure notebooks are currently free to use. You do not need to delete or shut down these items

For the Data Science VM, make sure you either:

* **Delete the VM:** remove the resource from your subscription and lose your work by deleting
![delete](./images/delete.JPG "delete") 
* **Shutdown the VM:** keep the VM setup and work but shut down the machine. This stops the cost of compute resources but you still pay for the storage of the VM
![shutdown](./images/stop.JPG "shutdown") 




