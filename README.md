## Welcome to ![LambdaTest Logo](https://www.lambdatest.com/resources/images/logos/logo.svg) - Python-UnitTest-Selenium Sample

---

### Step 1 : Virtual Environment Setup

ensure python3 is installed on your machine

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Step 2 : Setup Credentials

#### Lambdatest Credentials

Set LambdaTest username and access key in environment variables in the file `lamdatest.env`

Replace the values with your credentials, you can find them at (https://www.lambdatest.com/capabilities-generator/)

```
export LT_USERNAME="Your Username"
export LT_ACCESS_KEY="Your Access key"
```

![Lamdatest Credentials](/assets/screenshot.png)

After your save your credentials at `lambdatest.env` please run the command:

```
$ source lambdatest.env
```

### Step 3: Setting up your test capabilites

You can genegate the test capabilites at (https://www.lambdatest.com/capabilities-generator/) and choose **Python** as the language.

Now, can setup the capabilites of the test in the `single_test.py` file:

```
 lt_options = {
            "build": 'PyunitTest sample build',  # Change your build name here
            "name": 'Py-unittest',  # Change your test name here
            "platformName": 'Windows 10',  # Change your OS version here
            "browserName": 'chrome',  # Change your browser here
            "browserVersion": 'latest'  # Change your browser version here
        }
```

You can setup the capabilites of your test in the `parallel_test.py` file at:

```
browsers = [
    {"build": 'PyunitTest sample build', "name": "Test 1", "platform": "Windows 10", "browserName": "Chrome", "version": "latest"},
    {"build": 'PyunitTest sample build', "name": "Test 2", "platform": "Windows 10", "browserName": "edge", "version": "latest"},
    {"build": 'PyunitTest sample build', "name": "Test 3", "platform": "Windows 10", "browserName": "firefox", "version": "latest"}
]
```

### Step 4: Running Tests

To start a single test Run following command:

```
$ python single_test.py
```

<br/>

To start a parallel test Run the following command:

```
$ python parallel_test.py
```

<br/>

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.

### For further References

##### [SeleniumHQ Documentation](http://www.seleniumhq.org/docs/)

##### [UnitTest Documentation](https://docs.python.org/2/library/unittest.html)
