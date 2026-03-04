def encode_facility_rating( df ) :
    df['facility_rating'] = df['facility_rating'].map({
        'low' : 0, 'medium' : 1, 'high' : 2
    })
    return df
    
def encode_exam_difficulty( df ) :
    df['exam_difficulty'] = df['exam_difficulty'].map({
        'easy' : 0, 'moderate' : 1, 'hard' : 2
    })
    return df
