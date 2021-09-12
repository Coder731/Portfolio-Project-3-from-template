## flake8

from:
- [flake8 3.9.2 pip install flake8](https://pypi.org/project/flake8/)

pip install flake8

pip3 install flake8

Requirement already satisfied: flake8 in /home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/site-packages (3.9.2)

Requirement already satisfied: pycodestyle<2.8.0,>=2.7.0 in /home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/site-packages (from flake8) (2.7.0)

Requirement already satisfied: mccabe<0.7.0,>=0.6.0 in /home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/site-packages (from flake8) (0.6.1)

Requirement already satisfied: pyflakes<2.4.0,>=2.3.0 in /home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/site-packages (from flake8) (2.3.1)

- [](https://stackoverflow.com/questions/49270195/how-to-config-flake8-for-python-2-and-python-3-projects)


## node index.js
- this command is needed to view live preview
    - after running
        - npm install node index.js
            - and npm install -g npm
                - for upgrade

- Error:
    - in terminal:
        - Error as follows:

        internal/modules/cjs/loader.js:883
        throw err;
        ^

        Error: Cannot find module 'total4'
        Require stack:
        - /workspace/Portfolio-Project-3-from-template/index.js
            at Function.Module._resolveFilename (internal/modules/cjs/loader.js:880:15)
            at Function.Module._load (internal/modules/cjs/loader.js:725:27)
            at Module.require (internal/modules/cjs/loader.js:952:19)
            at require (internal/modules/cjs/helpers.js:88:18)
            at Object.<anonymous> (/workspace/Portfolio-Project-3-from-template/index.js:30:1)
            at Module._compile (internal/modules/cjs/loader.js:1063:30)
            at Object.Module._extensions..js (internal/modules/cjs/loader.js:1092:10)
            at Module.load (internal/modules/cjs/loader.js:928:32)
            at Function.Module._load (internal/modules/cjs/loader.js:769:14)
            at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:72:12) {
        code: 'MODULE_NOT_FOUND',
        requireStack: [ '/workspace/Portfolio-Project-3-from-template/index.js' ]
        }

- Next step:
    - search part of error as string:
        - internal/modules/cjs/loader.js:883 throw err; ^ Error: Cannot find module 'total4' Require stack:
    - result1:
        - [npm internal/modules/cjs/loader.js:883 throw err; ^ Error ...](https://github.com/nodejs/node/issues/38317)
    - result2:
        - [internal/modules/cjs/loader.js:800 throw err - Stack Overflow](https://stackoverflow.com/questions/60317962/internal-modules-cjs-loader-js800-throw-err)