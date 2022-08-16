<?php
include('connect.php');
//session_start();
$a = $_POST['offence_id'];
$b = $_POST['vehicle_no'];
$c = $_POST['driver_license'];
$d = $_POST['name'];
$e = $_POST['address'];
$f = $_POST['gender'];
$i = $_POST['phone'];
$g = $_POST['officer_reporting'];
$h = $_POST['offence'];
// query
$sql = "INSERT INTO reported_offence (offence_id,vehicle_no,driver_license,name,address,gender,phone,officer_reporting,offence,date ) VALUES (:a,:b,:c,:d,:e,:f,:i,:g,:h,now())";
$q = $db->prepare($sql);
$q->execute(array(':a'=>$a,':b'=>$b,':c'=>$c,':d'=>$d,':e'=>$e,':f'=>$f,':i'=>$i,':g'=>$g,':h'=>$h));{
if($q){
      header("location:report-offence.php?success=true");
        }else{
            header("location:report_offence.php?failed=true");
        } 
		}


?>
                            