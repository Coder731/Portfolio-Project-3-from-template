from:
    - see TESTING_excluded_debug.md


- try
    - using:
        - pip3 uninstall node_modules  and files and package-lock.json

- terminal returned:
    - the following four Warnings:
        WARNING: Skipping node-modules as it is not installed.
        WARNING: Skipping and as it is not installed.
        WARNING: Skipping files as it is not installed.
        WARNING: Skipping package-lock.json as it is not installed.

- try installing the elements referenced in previous four Warnings
    - note: the following are not modules, suggests syntax error / original command was pseudo-code
        - and 
        - files

- try installing:
    - node-modules
    - package-lock.json


- try:
    - pip3 install node-modules

- error:
    - as follows:
    ERROR: Could not find a version that satisfies the requirement node-modules (from versions: none)
    ERROR: No matching distribution found for node-modules

try:
    - npm install node-modules

returns:
    - the following:
        npm WARN old lockfile 
        npm WARN old lockfile The package-lock.json file was created with an old version of npm,
        npm WARN old lockfile so supplemental metadata must be fetched from the registry.
        npm WARN old lockfile 
        npm WARN old lockfile This is a one-time fix-up, please be patient...
        npm WARN old lockfile 
        npm WARN deprecated object-keys@0.2.0: Please update to the latest object-keys
        npm WARN deprecated cryptiles@0.2.2: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
        npm WARN deprecated sntp@0.2.4: This module moved to @hapi/sntp. Please make sure to switch over as this distribution is no longer supported and may contain bugs and critical security issues.
        npm WARN deprecated boom@0.4.2: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
        npm WARN deprecated hoek@0.9.1: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
        npm WARN deprecated node-uuid@1.4.8: Use uuid module instead
        npm WARN deprecated hawk@1.0.0: This module moved to @hapi/hawk. Please make sure to switch over as this distribution is no longer supported and may contain bugs and critical security issues.
        npm WARN deprecated request@2.27.0: request has been deprecated, see https://github.com/request/request/issues/3142

        added 47 packages, removed 1 package, and audited 51 packages in 10s

        14 vulnerabilities (3 low, 7 moderate, 4 high)

        To address issues that do not require attention, run:
        npm audit fix

        Some issues need review, and may require choosing
        a different dependency.

        Run `npm audit` for details.

- per third last option of returned result above:
- run:
    - npm audit fix

- returned:
    - the following:
        - herein:
        up to date, audited 51 packages in 990ms

        # npm audit report

        cryptiles  <=4.1.1
        Severity: high
        Insufficient Entropy - https://npmjs.com/advisories/1464
        Depends on vulnerable versions of boom
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/cryptiles
        hawk  <=6.0.2
        Depends on vulnerable versions of boom
        Depends on vulnerable versions of cryptiles
        Depends on vulnerable versions of hoek
        Depends on vulnerable versions of sntp
        node_modules/hawk
            request  2.2.6 - 2.80.0
            Depends on vulnerable versions of form-data
            Depends on vulnerable versions of hawk
            Depends on vulnerable versions of mime
            Depends on vulnerable versions of qs
            Depends on vulnerable versions of tunnel-agent
            node_modules/request
            node-modules  >=0.0.2
            Depends on vulnerable versions of optimist
            Depends on vulnerable versions of request
            node_modules/node-modules

        hawk  <=6.0.2
        Severity: high
        Regular Expression Denial of Service - https://npmjs.com/advisories/77
        Depends on vulnerable versions of boom
        Depends on vulnerable versions of cryptiles
        Depends on vulnerable versions of hoek
        Depends on vulnerable versions of sntp
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/hawk
        request  2.2.6 - 2.80.0
        Depends on vulnerable versions of form-data
        Depends on vulnerable versions of hawk
        Depends on vulnerable versions of mime
        Depends on vulnerable versions of qs
        Depends on vulnerable versions of tunnel-agent
        node_modules/request
            node-modules  >=0.0.2
            Depends on vulnerable versions of optimist
            Depends on vulnerable versions of request
            node_modules/node-modules

        hoek  <=4.2.0 || 5.0.0 - 5.0.2
        Severity: moderate
        Prototype Pollution - https://npmjs.com/advisories/566
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/hoek
        boom  <=3.1.2
        Depends on vulnerable versions of hoek
        node_modules/boom
            cryptiles  <=4.1.1
            Depends on vulnerable versions of boom
            node_modules/cryptiles
            hawk  <=6.0.2
            Depends on vulnerable versions of boom
            Depends on vulnerable versions of cryptiles
            Depends on vulnerable versions of hoek
            Depends on vulnerable versions of sntp
            node_modules/hawk
                request  2.2.6 - 2.80.0
                Depends on vulnerable versions of form-data
                Depends on vulnerable versions of hawk
                Depends on vulnerable versions of mime
                Depends on vulnerable versions of qs
                Depends on vulnerable versions of tunnel-agent
                node_modules/request
                node-modules  >=0.0.2
                Depends on vulnerable versions of optimist
                Depends on vulnerable versions of request
                node_modules/node-modules
        sntp  0.0.0 || 0.1.1 - 2.0.0
        Depends on vulnerable versions of hoek
        node_modules/sntp

        mime  <=1.4.0 || 2.0.1 - 2.0.2
        Severity: moderate
        Regular Expression Denial of Service - https://npmjs.com/advisories/535
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/form-data/node_modules/mime
        node_modules/request/node_modules/mime
        form-data  0.0.2 - 0.1.4
        Depends on vulnerable versions of mime
        node_modules/form-data
            request  2.2.6 - 2.80.0
            Depends on vulnerable versions of form-data
            Depends on vulnerable versions of hawk
            Depends on vulnerable versions of mime
            Depends on vulnerable versions of qs
            Depends on vulnerable versions of tunnel-agent
            node_modules/request
            node-modules  >=0.0.2
            Depends on vulnerable versions of optimist
            Depends on vulnerable versions of request
            node_modules/node-modules

        minimist  <0.2.1 || >=1.0.0 <1.2.3
        Prototype Pollution - https://npmjs.com/advisories/1179
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/minimist
        optimist  >=0.6.0
        Depends on vulnerable versions of minimist
        node_modules/optimist
            node-modules  >=0.0.2
            Depends on vulnerable versions of optimist
            Depends on vulnerable versions of request
            node_modules/node-modules

        node-static  *
        Unauthorized File Access - https://npmjs.com/advisories/1206
        No fix available
        node_modules/node-static

        qs  <=6.0.3 || 6.1.0 - 6.1.1 || 6.2.0 - 6.2.2 || 6.3.0 - 6.3.1
        Severity: high
        Prototype Pollution Protection Bypass - https://npmjs.com/advisories/1469
        Denial-of-Service Memory Exhaustion - https://npmjs.com/advisories/29
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/qs
        request  2.2.6 - 2.80.0
        Depends on vulnerable versions of form-data
        Depends on vulnerable versions of hawk
        Depends on vulnerable versions of mime
        Depends on vulnerable versions of qs
        Depends on vulnerable versions of tunnel-agent
        node_modules/request
            node-modules  >=0.0.2
            Depends on vulnerable versions of optimist
            Depends on vulnerable versions of request
            node_modules/node-modules

        request  2.2.6 - 2.80.0
        Severity: high
        Remote Memory Exposure - https://npmjs.com/advisories/309
        Depends on vulnerable versions of form-data
        Depends on vulnerable versions of hawk
        Depends on vulnerable versions of mime
        Depends on vulnerable versions of qs
        Depends on vulnerable versions of tunnel-agent
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/request
        node-modules  >=0.0.2
        Depends on vulnerable versions of optimist
        Depends on vulnerable versions of request
        node_modules/node-modules

        tunnel-agent  <0.6.0
        Severity: moderate
        Memory Exposure - https://npmjs.com/advisories/598
        fix available via `npm audit fix --force`
        Will install node-modules@0.0.1, which is a breaking change
        node_modules/tunnel-agent
        request  2.2.6 - 2.80.0
        Depends on vulnerable versions of form-data
        Depends on vulnerable versions of hawk
        Depends on vulnerable versions of mime
        Depends on vulnerable versions of qs
        Depends on vulnerable versions of tunnel-agent
        node_modules/request
            node-modules  >=0.0.2
            Depends on vulnerable versions of optimist
            Depends on vulnerable versions of request
            node_modules/node-modules

        14 vulnerabilities (3 low, 7 moderate, 4 high)

        To address all issues possible (including breaking changes), run:
        npm audit fix --force

        Some issues need review, and may require choosing
        a different dependency.

- do not commit these changes 
- try to repopen from github
then reopen in new gitpod workspace
from last commit.