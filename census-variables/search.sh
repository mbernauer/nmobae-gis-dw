perl -F'\t' -lane "print \"\$F[0]\t\$F[2]\t\$F[3]\" if \$F[3] =~ /$1/i & \$F[2] !~ /PE$/ & \$F[2] !~ /PR/" census_variables.tsv | sort -u
