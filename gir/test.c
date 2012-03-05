#include <stdio.h>

#include "anthygcontext.h"

int
main (int argc, char *argv[])
{
    AnthyGContext *obj = NULL;
    gchar *string = NULL;

    g_type_init ();

    obj = anthy_gcontext_new ();

    anthy_gcontext_set_encoding (obj, ANTHY_UTF8_ENCODING);
    anthy_gcontext_init_personality (obj);
    anthy_gcontext_do_set_personality(obj, "ibus__ibus_symbol");
    anthy_gcontext_set_string (obj, "てすと");
    anthy_gcontext_resize_segment (obj, 0, -1);
    printf ("%d\n", anthy_gcontext_get_nr_segments (obj));
    printf ("%d\n", anthy_gcontext_get_nr_candidates (obj, 0));
    string = anthy_gcontext_get_segment (obj, 0, 0);
    printf ("%s\n", string ? string : "(null)");
    anthy_gcontext_commit_segment (obj, 0, 0);
    anthy_gcontext_set_prediction_string (obj, "てすと");
    printf ("%d\n", anthy_gcontext_get_nr_predictions (obj));
    string = anthy_gcontext_get_prediction (obj, 0);
    printf ("%s\n", string ? string : "(null)");
    anthy_gcontext_commit_prediction (obj, 0);

    g_object_unref (obj);

    return 0;
}
