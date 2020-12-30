awk 'BEGIN {
print "Lines in log-file: ";
}
{
col++;
}
END {
print col;
}' $1
