#/bin/bash
mail --append="Content-type: text/html" -s "[PI Ping] $(curl -s -w '\n' ident.me)" mike@bridgecanada.com