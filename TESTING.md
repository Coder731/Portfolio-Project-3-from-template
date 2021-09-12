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

- From result2:
    - as follows:

    Solved Issue by checking NODE_OPTIONS

    Run echo %NODE_OPTIONS% and got ts-node/register.

- ran 
    - echo %NODE_OPTIONS%
- expected result per result2:
    - ts-node/register

- actual result:
    - %NODE_OPTIONS%
- note: this is the same as the original stringafter echo

- next step in result2 was:
    - to remove ts-node/register 
        - run setx NODE_OPTIONS ""

- however, as
    - ts-node/register
    - was not found:

- question whether to run:
    - setx NODE_OPTIONS ""

- also on result2:

    - as follows:
    Try following command:

    Step 1 : remove node_modules  and files and package-lock.json

    Then run following command to install dependencies:

    Step 2: $ rm -rf node_modules package-lock.json && npm install && npm start

    Finally, run your package by following command:

    npm start

- run
    - remove node_modules  and files and package-lock.json

- returned:
    - bash: remove: command not found

- run
    - pip3 install remove

- 2 errors
    ERROR: Could not find a version that satisfies the requirement remove (from versions: none)
    ERROR: No matching distribution found for remove

- searched error as string:
    - ERROR: Could not find a version that satisfies the requirement remove (from versions: none) ERROR: No matching distribution found for remove

- let result3 = 1st result of this search but 3rd in this debug sequence
    - [Fix the pip error: Couldn't find a version that satisfies ...](https://bhch.github.io/posts/2017/04/fix-the-pip-error-couldnt-find-a-version-that-satisfies-the-requirement/)

- result3
    - one potential cause ip address issue
        - use VPN
        - issue persists
        - rule out ip address issue

    - another potential cause:
        - PyPl server down

            - search 
                - how to check if PyPl server is down

            - [Is Pypl.org not opening?](https://sitedownornot.org/domain/Pypl.org)
                - Pypl.org is Up
                - rule out PyPl server down

search:
    - pip3 install remove

- let result 4 = 1st result of this search, but 4th in this debug sequence
    - [how to cleanly uninstall my python packages with pip3 or any other way?](https://stackoverflow.com/questions/29346217/how-to-cleanly-uninstall-my-python-packages-with-pip3-or-any-other-way)
        - mentions command:
            - pip3 uninstall abc

- instead of:
    - using
        - pip3 install remove
- try
    - using:
        - pip3 install uninstall

- error:
    - ERROR: Could not find a version that satisfies the requirement uninstall (from versions: none)
      ERROR: No matching distribution found for uninstall

- try
    - using:
        - instead of earlier command:
            - remove node_modules  and files and package-lock.json
        - try using:
            - uninstall node_modules  and files and package-lock.json

- error:
    - bash: uninstall: command not found
        - 

- The following code was run but resulted in errors, so was not committed, and continued testing/development/debug process from here instead.
    - code not committed (excluded) as follows:
        - see assets/documentation/TESTING_excluded_debug_files/TESTING_excluded_debug.md

- from:
    - [internal/modules/cjs/loader.js:800 throw err](https://stackoverflow.com/questions/60317962/internal-modules-cjs-loader-js800-throw-err#60320834)
        (from earlier in this debug sequence)
    - try running
        - rm -rf node_modules package-lock.json && npm install && npm start

- returned errors and warnings at the end of process:
    - as follows:
        > node@16.6.1 preinstall /workspace/Portfolio-Project-3-from-template/node_modules/node
        > node installArchSpecificPackage

        + node-linux-x64@16.6.1
        added 1 package in 1.934s
        found 0 vulnerabilities


        > node-pty@0.10.1 install /workspace/Portfolio-Project-3-from-template/node_modules/node-pty
        > node scripts/install.js

        (node:2581) [DEP0150] DeprecationWarning: Setting process.config is deprecated. In the future the property will be read-only.
        (Use `node --trace-deprecation ...` to show where the warning was created)
        make: Entering directory '/workspace/Portfolio-Project-3-from-template/node_modules/node-pty/build'
        CXX(target) Release/obj.target/pty/src/unix/pty.o
        ../src/unix/pty.cc: In function ‘void pty_after_waitpid(uv_async_t*)’:
        ../src/unix/pty.cc:512:43: warning: ‘void* memset(void*, int, size_t)’ writing to an object of type ‘class Nan::Persistent<v8::Function>’ with no trivial copy-assignment [-Wclass-memaccess]
        512 |   memset(&baton->cb, -1, sizeof(baton->cb));
            |                                           ^
        In file included from ../../nan/nan.h:407,
                        from ../src/unix/pty.cc:20:
        ../../nan/nan_persistent_12_inl.h:12:40: note: ‘class Nan::Persistent<v8::Function>’ declared here
        12 | template<typename T, typename M> class Persistent :
            |                                        ^~~~~~~~~~
        In file included from ../../nan/nan.h:58,
                        from ../src/unix/pty.cc:20:
        ../src/unix/pty.cc: At global scope:
        /home/gitpod/.cache/node-gyp/16.6.1/include/node/node.h:806:43: warning: cast between incompatible function types from ‘void (*)(Nan::ADDON_REGISTER_FUNCTION_ARGS_TYPE)’ {aka ‘void (*)(v8::Local<v8::Object>)’} to ‘node::addon_register_func’ {aka ‘void (*)(v8::Local<v8::Object>, v8::Local<v8::Value>, void*)’} [-Wcast-function-type]
        806 |       (node::addon_register_func) (regfunc),                          \
            |                                           ^
        /home/gitpod/.cache/node-gyp/16.6.1/include/node/node.h:840:3: note: in expansion of macro ‘NODE_MODULE_X’
        840 |   NODE_MODULE_X(modname, regfunc, NULL, 0)  // NOLINT (readability/null_usage)
            |   ^~~~~~~~~~~~~
        ../src/unix/pty.cc:734:1: note: in expansion of macro ‘NODE_MODULE’
        734 | NODE_MODULE(pty, init)
            | ^~~~~~~~~~~
        SOLINK_MODULE(target) Release/obj.target/pty.node
        COPY Release/pty.node
        make: Leaving directory '/workspace/Portfolio-Project-3-from-template/node_modules/node-pty/build'

        > node-pty@0.10.1 postinstall /workspace/Portfolio-Project-3-from-template/node_modules/node-pty
        > node scripts/post-install.js

        npm notice created a lockfile as package-lock.json. You should commit this file.
        added 12 packages from 20 contributors and audited 12 packages in 6.769s
        found 4 vulnerabilities (3 low, 1 high)
        run `npm audit fix` to fix them, or `npm audit` for details
        npm ERR! missing script: start

        npm ERR! A complete log of this run can be found in:
        npm ERR!     /home/gitpod/.npm/_logs/2021-09-12T19_20_59_020Z-debug.log