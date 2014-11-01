<html>
	<head>
		<meta http-equiv="refresh" content="5" >
	</head>
	<body>
	<?php
		$f = fopen("/var/www/temp.txt","r") or die ("unable to open file");
		echo "Temperature " . fgets($f) ;
		fclose ($f);
	?>
	</body>
</html>
