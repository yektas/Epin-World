     $(document).ready(function(){

          $("#mytable #checkall").click(function () {
                $("#mytable input[type=checkbox]").each(function () {
                    $(this).prop("checked", true);
               });

            } else {
                $("#mytable input[type=checkbox]").each(function () {
                    $(this).prop("checked", false);
              });
            }
        });

        $("[data-toggle=tooltip]").tooltip();
      });  