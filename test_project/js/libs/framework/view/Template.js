FJ.Template = function(templateString) {

    this.execute = function(element, params) {

        var ct = templateString.split("\n").join("");

        // STEP 1. Unroll loops
        for (var p in params) {

            if (typeof params[p] == "object") {
                var pattern = new RegExp('%for[(]' + p + '[)]%(.*?)%for%', 'g');
                var me = new RegExp('this', 'g');
                var match, matches = [];
                while ((match = pattern.exec(ct)) !== null) matches.push(match);

                for(var i = 0; i < matches.length; i++) {
                    match = matches[i];
                    var l = params[p];
                    var r = "";
                    var c = match[1];

                    for (var j = 0; j < l.length; j++) {
                        r += c.replace(me, "" + p + "[" + j + "]");
                    }

                    ct = ct.replace(match[0], r);
                }
            }
        }

        // Uncomment to DEBUG
//        element.innerHTML = ct;
//        return;

        // STEP 2. Check for conditional blocks and exclude parts that do not pass
        for (var p in params) {



            if (typeof params[p] == "boolean" || typeof params[p] == "object") {

                var pattern = new RegExp('%if[(]' + p + '([.|[][^%]*)[)]%', 'g');
                var match, matches = [];
                while ((match = pattern.exec(ct)) !== null) matches.push(match);

                for(var i = 0; i < matches.length; i++) {
                    match = matches[i];
                    var code = 'params[p]' + match[1];
                    var res;

                    try {
                        res = eval(code);
                        // TODO: Find more elegant way to evaluate that
                        res = (res == undefined || res == false) ? "false" : "true";
                    } catch(e) {
                        throw "TEMPLATE ERROR. Unable to call " + match[1] + " on '" + params[p] + "' (" + e + ")";
                    }

                    ct = ct.replace(match[0], '%if(' + res + ')%');
                }

                pattern = new RegExp('%if[(]' + p + '[)]%', 'g');
                matches = [];
                while ((match = pattern.exec(ct)) !== null) matches.push(match);

                for(var i = 0; i < matches.length; i++) {
                    ct = ct.replace(matches[i][0], '%if(' + params[p] + ')%');
                }

                var pattern = new RegExp('%if[(]true[)]%(.*?)%if%', 'g');
                var match, matches = [];
                while ((match = pattern.exec(ct)) !== null) matches.push(match);

                for(var i = 0; i < matches.length; i++) {
                    ct = ct.replace(matches[i][0], matches[i][1]);
                }

                var pattern = new RegExp('%if[(]false[)]%(.*?)%if%', 'g');
                var match, matches = [];
                while ((match = pattern.exec(ct)) !== null) matches.push(match);

                for(var i = 0; i < matches.length; i++) {
                    ct = ct.replace(matches[i][0], '');
                }
            }
        }

        // Uncomment to DEBUG
//        element.innerHTML = ct;
//        return;

        // STEP 3. Match all remaining simple strings
        for (var p in params) {

            if (typeof params[p] == "string" || typeof params[p] == "object") {

                // Look for complex expressions first...
                var pattern = new RegExp('%' + p + '([.|[][^%]*)%', 'g');
                var match, matches = [];
                while ((match = pattern.exec(ct)) !== null) matches.push(match);

                for(var i = 0; i < matches.length; i++) {
                    match = matches[i];
                    var code = 'params[p]' + match[1];
                    var res;

                    try {
                        res = eval(code);
                    } catch(e) {
                        throw "TEMPLATE ERROR. Unable to call " + match[1] + " on '" + params[p] + "' (" + e + ")";
                    }

                    ct = ct.replace(match[0], res);
                }

                // ...then look for plain expressions
                pattern = new RegExp('%' + p + '%', 'g');
                matches = [];
                while ((match = pattern.exec(ct)) !== null) matches.push(match);

                for(var i = 0; i < matches.length; i++) {
                    ct = ct.replace(matches[i][0], params[p]);
                }
            }
        }

	    // TODO - maybe we should add an argument that determines where the html will be added (before, after, replace)
	    // or at least throw a warning if the template is going to overwrite content. It's very hard to debug.

	    // don't want to overwrite body, so append it with the template
	    if (element == document.body) {
		    document.body.insertAdjacentHTML("beforeend", ct);
	    } else {
		    element.innerHTML = ct;
	    }

    }

};