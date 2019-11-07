<!--Programma creato da Francesco Ciociola - https://kekko01.altervista.org - 2019 GitHub: https://GitHub.com/Kekko01!-->
<!DOCTYPE html>
<html lang="it" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>CALCOLO PREZZI by Kekko01</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </head>
  <body>
    <div class="container-fluid">
      <h3>CALCOLO PREZZI</h3>
      <form class="" action="<?php echo $_PHP['SELF']; ?>" method="post">
        <div class="form-row">
          <div class="col-3">
            <input type="number" class="form-control" placeholder="Percentuale Guadagno" name="percguadagno" required>
          </div>
          <div class="col">
            <input type="number" class="form-control" placeholder="Sconto 1" name="sconto1">
          </div>
          <div class="col">
            <input type="number" class="form-control" placeholder="Sconto 2" name="sconto2">
          </div>
          <div class="col">
            <input type="number" class="form-control" placeholder="Sconto 3" name="sconto3">
          </div>
          <div class="col">
            <input type="number" class="form-control" placeholder="Sconto 4" name="sconto4">
        </div><br>
        <div class="form-row align-items-center">
          <div class="col-sm-3 my-1">
            <label class="sr-only" for="inlineFormInputName">Importo del Venditore</label>
            <input type="number" class="form-control" id="inlineFormInputName" name="importo" required>
          </div>
          <div class="col-auto my-1">
            <button type="submit" class="btn btn-primary">Calcola</button>
          </div>
        </div>
      </form>
      <?php
        if (isset($_POST)) {
          $percguadagno=$_POST['percguadagno']/100;
          $sconto1=$_POST['sconto1']/100;
          $sconto2=$_POST['sconto2']/100;
          $sconto3=$_POST['sconto3']/100;
          $sconto4=$_POST['sconto4']/100;
          $importo=$_POST['importo'];
          $totale=$importo;
          $totale=$totale-$totale*$sconto1;
          $totale=$totale-$totale*$sconto2;
          $totale=$totale-$totale*$sconto3;
          $totale=$totale-$totale*$sconto4;
          $totale=$totale+$totale*$percguadagno;
          $iva=0.22;
          $totale=$totale+$totale*$iva;
          echo "Il totale e' di: ",$totale;
        }


       ?>
    </div>
    <div class="alert alert-primary" role="alert">
      Creato da <a href="https://kekko01.altervista.org" class="alert-link">Kekko01</a>. Buon uso!
    </div>
  </body>
</html>
