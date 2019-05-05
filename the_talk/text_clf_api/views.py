from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextSerializer
from .predictors import predict, predict_proba


class Api(APIView):

    def map_result_to_json(self, preds, probas):
        clf_names = ['agg', 'obs', 'spm']
        json = {}
        for i in range(len(preds[0])):
            result = {}
            for j in range(len(clf_names)):
                clf = {}
                clf['pred'] = preds[j][i]
                clf['prob_0'] = probas[j][i][0]
                clf['prob_1'] = probas[j][i][1]
                result[clf_names[j]] = clf

            json[str(i)] = result
        return json

    def post(self, request):
        serializer = TextSerializer(data=request.data)

        if serializer.is_valid():
            texts = serializer.data['texts']

            preds = predict(texts)
            probas = predict_proba(texts)

            return Response(self.map_result_to_json(preds, probas), headers={
                'Access-Control-Allow-Origin': '*'
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST,
                            headers={
                                'Access-Control-Allow-Origin': '*'
                            })
