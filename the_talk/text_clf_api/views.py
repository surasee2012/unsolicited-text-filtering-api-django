from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReqSerializer
from .predictors import predict, predict_proba


class Api(APIView):

    def map_result_to_json(self, clfs, preds, probas=None):
        json = {}
        for i in range(len(preds[0])):
            result = {}
            for j in range(len(clfs)):
                clf = {}
                clf['pred'] = preds[j][i]
                if (probas != None):
                    clf['prob_0'] = probas[j][i][0]
                    clf['prob_1'] = probas[j][i][1]
                result[clfs[j]] = clf

            json["t" + str(i)] = result
        return json

    def post(self, request):
        serializer = ReqSerializer(data=request.data)

        if serializer.is_valid():
            clfs = serializer.data['clfs']
            prob = serializer.data['prob']
            texts = serializer.data['texts']
            if (clfs == ['*']):
                clfs = ["agg", "obs", "spm"]

            preds = predict(clfs, texts)
            probas = None
            if (prob):
                probas = predict_proba(clfs, texts)

            return Response(self.map_result_to_json(clfs, preds, probas), headers={
                'Access-Control-Allow-Origin': '*'
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST,
                            headers={
                                'Access-Control-Allow-Origin': '*'
                            })
