from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextSerializer
from .predictors import predict

class Api(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)

        if serializer.is_valid():
            text = serializer.data['text']
            
            predict_result = predict(text)

            return Response({
                'agg': {
                    'result': predict_result[0][0],
                    '0_prob': predict_result[0][1][0],
                    '1_prob': predict_result[0][1][1],
                },
                'obs': {
                    'result': predict_result[1][0],
                    '0_prob': predict_result[1][1][0],
                    '1_prob': predict_result[1][1][1],
                },
                'spm': {
                    'result': predict_result[2][0],
                    '0_prob': predict_result[2][1][0],
                    '1_prob': predict_result[2][1][1],
                }
                })
        else:
            return Response(serializer.errors,
                            status='status.HTTP_40HTTP_400_BAD_REQUEST')