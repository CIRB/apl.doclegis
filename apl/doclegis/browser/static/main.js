var oTable;

(function($) {
/*
 * Function: fnGetColumnData
 * Purpose:  Return an array of table values from a particular column.
 * Returns:  array string: 1d data array
 * Inputs:   object:oSettings - dataTable settings object. This is always the last argument past to the function
 *           int:iColumn - the id of the column to extract the data from
 *           bool:bUnique - optional - if set to false duplicated values are not filtered out
 *           bool:bFiltered - optional - if set to false all the table data is used (not only the filtered)
 *           bool:bIgnoreEmpty - optional - if set to false empty values are not filtered from the result array
 * Author:   Benedikt Forchhammer <b.forchhammer /AT\ mind2.de>
 */
$.fn.dataTableExt.oApi.fnGetColumnData = function ( oSettings, iColumn, bUnique, bFiltered, bIgnoreEmpty ) {
    // check that we have a column id
    if ( typeof iColumn == "undefined" ) return new Array();
     
    // by default we only want unique data
    if ( typeof bUnique == "undefined" ) bUnique = true;
     
    // by default we do want to only look at filtered data
    if ( typeof bFiltered == "undefined" ) bFiltered = true;
     
    // by default we do not want to include empty values
    if ( typeof bIgnoreEmpty == "undefined" ) bIgnoreEmpty = true;
     
    // list of rows which we're going to loop through
    var aiRows;
     
    // use only filtered rows
    if (bFiltered == true) aiRows = oSettings.aiDisplay;
    // use all rows
    else aiRows = oSettings.aiDisplayMaster; // all row numbers
 
    // set up data array   
    var asResultData = new Array();
     
    for (var i=0,c=aiRows.length; i<c; i++) {
        iRow = aiRows[i];
        var aData = this.fnGetData(iRow);
        var sValue = aData[iColumn];
         
        // ignore empty values?
        if (bIgnoreEmpty == true && sValue.length == 0) continue;
 
        // ignore unique values?
        else if (bUnique == true && jQuery.inArray(sValue, asResultData) > -1) continue;
         
        // else push the value onto the result data array
        else asResultData.push(sValue);
    }
     
    return asResultData;
}}(jQuery));
 
 
function fnCreateSelect( aData )
{
    var r='<select><option value=""></option>', i, iLen=aData.length;
    for ( i=0 ; i<iLen ; i++ )
    {
        r += '<option value="'+aData[i]+'">'+aData[i]+'</option>';
    }
    return r+'</select>';
}
 
function eliminateDuplicates(arr) {
  var i,
      len=arr.length,
      out=[],
      obj={};

  for (i=0;i<len;i++) {
    obj[arr[i]]=0;
  }
  for (i in obj) {
    out.push(i);
  }
  return out;
}

function getListValue(numcols) {
	out=[];
	list=[];
	coldata = oTable.fnGetColumnData(numcols);
	for (var i=0;i<coldata.length;i++){
		elems = coldata[i].split(',')
		for (var j=0; j<elems.length; ++j){
			elem = $.trim(elems[j])
			if (elem != ''){
				out.push(elem)
			}
		}
	}
	
	return eliminateDuplicates(out);
}

$(document).ready(function() {
    /* Initialise the DataTable */
    oTable = $('#doclegisTable').dataTable( {
        "oLanguage": {
            "sUrl": "++resource++doclegis/datatables_"+$('html').attr('lang')+""
        },
        "aoColumnDefs": [
        	{"bVisible": false, "aTargets": [3, 4, 5, 6]},
        ],
    });
    
     
    $('div#filter_document_type').html(
    	fnCreateSelect( oTable.fnGetColumnData(1) ));
    $('select', 'div#filter_document_type').change( 
    	function () {
            oTable.fnFilter( $(this).val(), 1 );
     	}
     );

    $('div#filter_theme').html(
    	fnCreateSelect( getListValue(4) ));
    $('select', 'div#filter_theme').change( 
    	function () {
            oTable.fnFilter( $(this).val(), 4 );
     	}
     );

    $('div#filter_year').html(
    	fnCreateSelect( oTable.fnGetColumnData(3) ));
    $('select', 'div#filter_year').change( 
    	function () {
            oTable.fnFilter( $(this).val(), 3 );
     	}
     );

    $('div#filter_institution').html(
    	fnCreateSelect( getListValue(5) ));
    $('select', 'div#filter_institution').change( 
    	function () {
    		val = $(this).val();
            oTable.fnFilter(val, 5 );
            if (val == "Communes" ||  val == "CPAS" ||
            	val == 'Gemeenten' || val == "OCMW"
            	){
            	$('#spantohid').show();
            } else {
            	$('#spantohid').hide();
            }
     	}
     );
    $('#spantohid').hide();

    $('div#filter_commune').html(
    	fnCreateSelect( getListValue(6) ));
    $('select', 'div#filter_commune').change( 
    	function () {
            oTable.fnFilter( $(this).val(), 6 );
     	}
     );

} );
