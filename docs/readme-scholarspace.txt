readme-scholarspace.txt

NFLRC (community)
- Language Learning and Technology (community)
    - Volume (1 to n-1) (collection)


Vocabularies
type - (note distinction between TYPE and TYPE.DCMI) type is field designated for indicating that a collection item is part of a section within an issue. These sections should be labeled with one of the following:
    * Front Matter (items that appear at the beginning of issue.)
    * Column (items that group under a "column" title specified in related llt.topic field)
    * Article (items that group under ordinary issue submissions )
    * Review (items that are a review)

llt.topic - indicates the title of a column under which an item should be grouped

dc.contributor.editor - indicates that an item as a distinct editor(s)

sketch

ITEM_DESC = ['REC OBJECT', 'AUTHOR LIST', 'ABSTRACT TEXT', 'PAGE START']

{
    TYPE_NAME: {
        "subkey_a": [ITEM_DESC, ITEM_DESC, ITEM_DESC, ...],
        "subkey_a": [ITEM_DESC, ITEM_DESC, ITEM_DESC, ...],
        ...
    },
            }
}


Example:
ITEM_DESC = ['REC OBJECT', 'AUTHOR LIST', 'ABSTRACT TEXT', 'PAGE START']
toc = {
'ARTICLE': {'': {"editors": [], "records": [ ITEM_DESC, ITEM_DESC, ITEM_DESC, ]}},
'COLUMN': {
    'llt_topic_a': {"editors": [], "records":  [ ITEM_DESC, ITEM_DESC, ITEM_DESC,  ]},
    'llt_topic_b': {"editors": [], "records":  [ ITEM_DESC, ITEM_DESC, ITEM_DESC, ]},
},
'REVIEW': {
    'llt_topic_a': {"editors": [], "records":  [ ITEM_DESC, ITEM_DESC, ITEM_DESC, ]},
    'llt_topic_b': {"editors": [], "records":  [ ITEM_DESC, ITEM_DESC, ITEM_DESC, ]},
},
'FRONT_MATTER': {'': {"editors": [], "records":  [ ITEM_DESC, ITEM_DESC, ITEM_DESC, ]}}
}




    