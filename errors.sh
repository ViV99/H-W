awk 'BEGIN {
print "Errors in log-file:"
}

{
if ($2 == "ERROR")
        print($0);
}' $1
