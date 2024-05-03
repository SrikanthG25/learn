class DayEndBillReportView(generics.GenericAPIView):
    # permission_classes = (permissions.AllowAny,)
    def get(self,request):
        """
        URL - fo/dayend/bill/report/?export_type=&module_type=op,ip,lab,pharmacy&payment_method=1,2,3,4,5&from_date=2023-02-23&to_date=2023-05-29
        Sample Response
        {
            "status": "success",
            "message": "Day end bill report",
            "data": {
                "cash_amount": 40.0,
                "card_amount": 40.0,
                "upi_amount": 40.0,
                "bank_amount": 40.0,
                "cheque_amount": 40.0,
                "insurance_amount": 0,
                "total_amount": 200.0,
                "data": [
                    {
                        "bill_type": "Out Patient",
                        "cash": 20.0,
                        "card": 20.0,
                        "upi": 20.0,
                        "bank_transfer": 20.0,
                        "cheque": 20.0,
                        "insurance": 0,
                        "total": 100.0
                    },
                    {
                        "bill_type": "In Patient",
                        "cash": 20.0,
                        "card": 20.0,
                        "upi": 20.0,
                        "bank_transfer": 20.0,
                        "cheque": 20.0,
                        "insurance": 0,
                        "total": 100.0
                    },
                    {
                        "bill_type": "Laboratory",
                        "cash": 0,
                        "card": 0,
                        "upi": 0,
                        "bank_transfer": 0,
                        "cheque": 0,
                        "insurance": 0,
                        "total": 0
                    },
                    {
                        "bill_type": "Pharmacy",
                        "cash": 0,
                        "card": 0,
                        "upi": 0,
                        "bank_transfer": 0,
                        "cheque": 0,
                        "insurance": 0,
                        "total": 0
                    }
                ]
            }
        }
        """
        try:
            data = request.GET
            clinic_id = request.clinic_id
            export_type = data.get('export_type')
            from_date = data.get('from_date')
            to_date = data.get('to_date')
            start_time = data.get('start_time')
            end_time = data.get('end_time')
            user_id = data.get('user_id')
            ph_search={}
            search_data = {}
            exp_search = {}
            api_start_time = time.time()
            models = data.get('module_type').split(',') if data.get('module_type') else False
            if not models:
                return Response({'status': 'fail', 'message': 'Please select modules'},status=status.HTTP_400_BAD_REQUEST)
            if user_id:
                user_ids = [int(user) for user in user_id.split(',')]
            payment_type = []
            if data.get('payment_method'):
                payment_type = [int(i) for i in data.get('payment_method').split(',')]

            if start_time and end_time:
                search_data['invoice_date__gte'] = datetime.combine(datetime.strptime(from_date, '%Y-%m-%d').date(),datetime.strptime(start_time,"%H:%M:%S").time())
                search_data['invoice_date__lte'] = datetime.combine(datetime.strptime(to_date, '%Y-%m-%d').date(),datetime.strptime(end_time,"%H:%M:%S").time())
                ph_search['invoice_date__gte'] = search_data['invoice_date__gte']
                ph_search['invoice_date__lte'] = search_data['invoice_date__lte']
                exp_search['bill_date__gte']=from_date
                exp_search['bill_date__lte']=to_date
                # logger.info('Date Check {} - {}'.format(ph_search['created_date__gte'],ph_search['created_date__lte']))

            elif from_date and to_date:
                search_data['invoice_date__date__gte'] = from_date
                search_data['invoice_date__date__lte'] = to_date
                ph_search['invoice_date__date__gte']=from_date
                ph_search['invoice_date__date__lte']=to_date
                exp_search['bill_date__date__gte']=from_date
                exp_search['bill_date__date__lte']=to_date
                ph_search['invoice_date__date__lte']=to_date
            if user_id:
                search_data['login_user_id__in'] = user_ids
                ph_search['login_user_id__in']=user_ids
                exp_search['login_user_id__in'] = user_ids
            mode_search = []
            if 1 in payment_type:
                mode_search.append('cash')
            if 2 in payment_type:
                mode_search.append('card')
            if 3 in payment_type:
                mode_search.append('upi')
            if 4 in payment_type:
                mode_search.append('cheque')
            if 5 in payment_type:
                mode_search.append('bank')
            if 6 in payment_type:
                mode_search.append('insurance')

            result = {
                "cash_amount" : 0,
                "card_amount" : 0,
                "upi_amount" : 0,
                "bank_amount" : 0,
                "cheque_amount" : 0,
                "insurance_amount" : 0,
                "total_amount" : 0,            
                "total_credit_value" : 0,            
                "data": [
                    {
                        "bill_type" : "Out Patient",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "bank_transfer" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    },
                    {
                        "bill_type" : "In Patient",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "bank_transfer" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    },
                    {
                        "bill_type" : "Laboratory",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "bank_transfer" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    },
                    {
                        "bill_type" : "Pharmacy",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "bank_transfer" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    },
                    {
                        "bill_type" : "FO Laboratory",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "bank_transfer" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    },
                    {
                        "bill_type" : "FO Pharmacy",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "bank_transfer" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    },
                    {
                        "bill_type" : "Expenses",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "bank_transfer" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    },
                    {
                        "bill_type" : "OT",
                        "cash" : 0,
                        "card" : 0,
                        "upi" : 0,
                        "cheque" : 0,
                        "insurance" : 0,
                        "bank_transfer" : 0,
                        "total" : 0,
                        "credit_value" : 0
                    }
                ]
            }

            branch_id = Clinic.objects.filter(clinic_id=clinic_id).values_list('branch_detail_id',flat=True)
            allow_pharmacy_bills = CustomConfig.objects.get(clinic_id=clinic_id).show_pharmacy_bills_in_fo
            currency = Configuration.objects.get(clinic_id=clinic_id)
            op_credit = Invoice.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(net_amount=Sum(F('amount_net')-F('received_amount'),output_field=DecimalField()))
            if op_credit:
                result['data'][0]['credit_value'] = op_credit[0]['net_amount']
                result['total_credit_value'] += op_credit[0]['net_amount']
            ip_credit = InpatientBillingSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(net_amount=Sum(F('net_amount')-F('received_amount'),output_field=DecimalField()))
            if ip_credit:
                result['data'][1]['credit_value'] = ip_credit[0]['net_amount'] 
                result['total_credit_value'] += ip_credit[0]['net_amount'] 
            lab_credit = LabBillSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(net_amount=Sum(F('net_amount')-F('received_amount'),output_field=DecimalField()))
            if lab_credit:
                result['data'][2]['credit_value'] = lab_credit[0]['net_amount']
                result['total_credit_value'] += Decimal(lab_credit[0]['net_amount'])
            if allow_pharmacy_bills:
                ip_pharmacy_credit = PharmacyBillSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',ip_admission__isnull=False,**search_data).values('bill_type').annotate(net_amount=Sum(F('net_amount')-F('received_amount'),output_field=DecimalField()))
                if ip_pharmacy_credit:
                    result['data'][3]['credit_value'] = ip_pharmacy_credit[0]['net_amount'] 
                    result['total_credit_value'] += Decimal(ip_pharmacy_credit[0]['net_amount'])
                op_pharmacy_credit = PharmacyBillSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',ip_admission__isnull=True,**search_data).values('bill_type').annotate(net_amount=Sum(F('net_amount')-F('received_amount'),output_field=DecimalField()))
                if op_pharmacy_credit:
                    result['data'][4]['credit_value'] = op_pharmacy_credit[0]['net_amount'] 
                    result['total_credit_value'] += Decimal(op_pharmacy_credit[0]['net_amount'])
            ot_credit = OtBillingSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(net_amount=Sum(F('total_net_amount')-F('received_amount'),output_field=DecimalField()))
            if ot_credit:
                result['data'][7]['credit_value'] = ot_credit[0]['net_amount'] 
                result['total_credit_value'] += ot_credit[0]['net_amount'] 
            receipt = BillingReceiptNumber.objects.filter(branch_id__in=branch_id,**search_data).values('id','created_by','receipt_type','receipt_for','paid_for','collected_in','created_date','insurance_amount','advance_amount','module_id','receipt_number','receipt_sequence','payment_mode','amount_received','invoice_date',
                                                                'payment_mode_types','amount_cash','amount_card','upi_amount','bank_transfer_amount','cheque_amount','patient_id',patient_names = F('patient__first_name'),patient_uhid=F('patient__patient_account_number'))
            expense = ExpenseBill.objects.filter(**exp_search,clinic_id=clinic_id,is_active=True).values('payment_type').annotate(Sum('amount'))
            exp_total = 0
            for exp in expense:
                exp_total += exp['amount__sum']
                if exp['payment_type'] == '1':
                    result['data'][6]['cash'] = exp['amount__sum']
                elif exp['payment_type'] == '2':
                    result['data'][6]['card'] = exp['amount__sum']
                elif exp['payment_type'] == '3':
                    result['data'][6]['upi'] = exp['amount__sum']
                elif exp['payment_type'] == '5':
                    result['data'][6]['bank_transfer'] = exp['amount__sum']
            result['data'][6]['total'] = exp_total

            credit_invoice_data = list(Invoice.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(module=Value(str('Out Patient')),company_name=F('patient__insurance_company_name'),corporate_name=F('employer__company_name'),pending_amount=Sum(F('amount_net')-F('received_amount'), output_field=FloatField())))
            credit_ip_data = list(InpatientBillingSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(company_name=F('insurance_company_name'),corporate_name=F('employer__company_name'),module=Value('In Patient'),pending_amount=Sum(F('net_amount')-F('received_amount'), output_field=FloatField())))
            credit_lab_data = list(LabBillSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(company_name=F('insurance_company_name'),module=Value(str('Laboratory')),corporate_name=F('employer__company_name'),pending_amount=Sum(F('net_amount')-F('received_amount'), output_field=FloatField())))
            credit_invoice_data.extend(credit_ip_data)
            credit_invoice_data.extend(credit_lab_data)

            cancel_invoice_data = list(Invoice.objects.filter(clinic_id=clinic_id,bill_type='cancelled',**search_data).values('bill_type').annotate(module=Value(str('Out Patient')),cancelled_amount=Sum('amount_net', output_field=FloatField()),bill_count=Count('bill_type')))
            cancel_ip_data = list(InpatientBillingSummary.objects.filter(clinic_id=clinic_id,bill_type='cancelled',**search_data).values('bill_type').annotate(module=Value(str('In Patient')),cancelled_amount=Sum('net_amount', output_field=FloatField()),bill_count=Count('bill_type')))
            cancel_lab_data = list(LabBillSummary.objects.filter(clinic_id=clinic_id,bill_type='cancelled',**search_data).values('bill_type').annotate(module=Value(str('Laboratory')),cancelled_amount=Sum('net_amount', output_field=FloatField()),bill_count=Count('bill_type')))
            cancel_invoice_data.extend(cancel_ip_data)
            cancel_invoice_data.extend(cancel_lab_data)
            
            if allow_pharmacy_bills:
                credit_pharmacy_data = PharmacyBillSummary.objects.filter(clinic_id=clinic_id,bill_type='credit',**search_data).values('bill_type').annotate(company_name=F('insurance_company_name'),module=Value('Pharmacy'),corporate_name=F('employer__company_name'),pending_amount=Sum(F('net_amount')-F('received_amount'), output_field=FloatField()))
                credit_invoice_data.extend(credit_pharmacy_data)
                cancel_pharmacy_data = list(PharmacyBillSummary.objects.filter(clinic_id=clinic_id,bill_type='Return',**search_data).values('bill_type').annotate(module=Value(str('Pharmacy')),cancelled_amount=Sum('net_amount', output_field=FloatField()),bill_count=Count('bill_type')))
                cancel_invoice_data.extend(cancel_pharmacy_data)
                
            # credit_data = {}
            cancell_data = {}
            # final_credit_data = []     

            # for i in  credit_invoice_data:  #ip/op/lab/pharmacy summary iteration
            #     key = "{}_{}".format(i['module'],i['credit_type'])
            #     if key in credit_data.keys():
            #         credit_data[key]['pending_amount'] += i['pending_amount']
            #     else:
            #         credit_data[key] = i
            # final_credit_data = credit_data.values()

            # pharmacy_bill_summery=PharmacyBillSummary.objects.filter(~Q(bill_type__in=['cancelled','canceled']),clinic_id=clinic_id,**ph_search).values('id','invoice_date','patient_id','billing_status','patient_account_number','upi_amount','bill_type','cheque_amount','insurance_amount','payment_mode','balance_amount',amount_cash=F('cash_amount'),bank_transfer_amount=F('bank_amount'),amount_card=F('card_amount'),amount_paid=F('received_amount'),bill_number=F('invoice_number'),amount_net=F('grand_total')) 
            # if 'pharmacy' in models:
            #     for p in pharmacy_bill_summery:
            #         if p['billing_status'] != "Returned":
            #             if 'cash' in mode_search:
            #                 result['data'][3]['cash'] +=Decimal( p['amount_cash'])
            #                 result['cash_amount'] += Decimal(p['amount_cash'])
            #             if 'card' in mode_search:
            #                 result['data'][3]['card'] += Decimal(p['amount_card'])
            #                 result['card_amount'] +=Decimal( p['amount_card'])
            #             if 'upi' in mode_search:
            #                 result['data'][3]['upi'] += Decimal(p['upi_amount'])
            #                 result['upi_amount'] += Decimal(p['upi_amount'])
            #             if 'bank' in mode_search:
            #                 result['data'][3]['bank_transfer'] += Decimal(p['bank_transfer_amount'])
            #                 result['bank_amount'] += Decimal(p['bank_transfer_amount'])
            #             if 'cheque' in mode_search:
            #                 result['data'][3]['cheque'] += Decimal(p['cheque_amount'])
            #                 result['cheque_amount'] += Decimal(p['cheque_amount'])
            #             if 'insurance' in mode_search:
            #                 result['data'][3]['insurance'] += Decimal(p['insurance_amount'])
            #                 result['insurance_amount'] +=  Decimal(p['insurance_amount'])
                        
            #         elif p['billing_status'] == "Returned" :
            #             if 'cash' in mode_search:
            #                 result['data'][3]['cash'] -= Decimal(p['amount_cash'])
            #                 result['cash_amount'] -= Decimal(p['amount_cash'])
            #             if 'card' in mode_search:
            #                 result['data'][3]['card'] -= Decimal(p['amount_card'])
            #                 result['card_amount'] -= Decimal(p['amount_card'])
            #             if 'upi' in mode_search:
            #                 result['data'][3]['upi'] -= Decimal(p['upi_amount'])
            #                 result['upi_amount'] -= Decimal(p['upi_amount'])
            #             if 'bank' in mode_search:
            #                 result['data'][3]['bank_transfer'] -=Decimal( p['bank_transfer_amount'])
            #                 result['bank_amount'] -= Decimal(p['bank_transfer_amount'])
            #             if 'cheque' in mode_search:
            #                 result['data'][3]['cheque'] -= Decimal(p['cheque_amount'])
            #                 result['cheque_amount'] -= Decimal(p['cheque_amount'])
            #             if 'insurance' in mode_search:
            #                 result['data'][3]['insurance'] -=  Decimal(p['insurance_amount'])
            #                 result['insurance_amount'] -=  Decimal(p['insurance_amount'])
            #         else:
            #             pass
            #         result['data'][3]['total'] = result['data'][3]['cash'] + result['data'][3]['card'] + result['data'][3]['upi'] + result['data'][3]['bank_transfer'] + result['data'][3]['cheque'] + result['data'][3]['insurance']
            for i in receipt:
                i['patient_name'] = i['patient_names']
                del i['patient_names']
                if payment_type and i['payment_mode']:
                    if 'op' in models:
                        if i['collected_in'] == 'OP':
                            if i['receipt_for'] not in ['Refund','Cancelled']:
                                if 'cash' in mode_search:
                                    result['data'][0]['cash'] += i['amount_cash']
                                    result['cash_amount'] += i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][0]['card'] += i['amount_card']
                                    result['card_amount'] += i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][0]['upi'] += i['upi_amount']
                                    result['upi_amount'] += i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][0]['bank_transfer'] += i['bank_transfer_amount']
                                    result['bank_amount'] += i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][0]['cheque'] += i['cheque_amount']
                                    result['cheque_amount'] += i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][0]['insurance'] += i['insurance_amount']
                                    result['insurance_amount'] += i['insurance_amount']
                            else:
                                if 'cash' in mode_search:
                                    result['data'][0]['cash'] -= i['amount_cash']
                                    result['cash_amount'] -= i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][0]['card'] -= i['amount_card']
                                    result['card_amount'] -= i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][0]['upi'] -= i['upi_amount']
                                    result['upi_amount'] -= i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][0]['bank_transfer'] -= i['bank_transfer_amount']
                                    result['bank_amount'] -= i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][0]['cheque'] -= i['cheque_amount']
                                    result['cheque_amount'] -= i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][0]['insurance'] -= i['insurance_amount']
                                    result['insurance_amount'] -= i['insurance_amount']
                            result['data'][0]['total'] = result['data'][0]['cash'] + result['data'][0]['card'] + result['data'][0]['upi'] + result['data'][0]['bank_transfer'] + result['data'][0]['cheque'] + result['data'][0]['insurance']
                    if 'ip' in models or 'ot' in models:
                        if i['collected_in'] == 'IP':
                            if i['receipt_for'] not in ['Refund','Cancelled','Advance refund']:
                                if 'cash' in mode_search:
                                    result['data'][1]['cash'] += i['amount_cash']
                                    result['cash_amount'] += i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][1]['card'] += i['amount_card']
                                    result['card_amount'] += i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][1]['upi'] += i['upi_amount']
                                    result['upi_amount'] += i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][1]['bank_transfer'] += i['bank_transfer_amount']
                                    result['bank_amount'] += i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][1]['cheque'] += i['cheque_amount']
                                    result['cheque_amount'] += i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][1]['insurance'] += i['insurance_amount']
                                    result['insurance_amount'] += i['insurance_amount']
                            else:
                                if 'cash' in mode_search:
                                    result['data'][1]['cash'] -= i['amount_cash']
                                    result['cash_amount'] -= i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][1]['card'] -= i['amount_card']
                                    result['card_amount'] -= i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][1]['upi'] -= i['upi_amount']
                                    result['upi_amount'] -= i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][1]['bank_transfer'] -= i['bank_transfer_amount']
                                    result['bank_amount'] -= i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][1]['cheque'] -= i['cheque_amount']
                                    result['cheque_amount'] -= i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][1]['insurance'] -= i['insurance_amount']
                                    result['insurance_amount'] -= i['insurance_amount']
                            result['data'][1]['total'] = result['data'][1]['cash'] + result['data'][1]['card'] + result['data'][1]['upi'] + result['data'][1]['bank_transfer'] + result['data'][1]['cheque'] + result['data'][1]['insurance']
                    if 'lab' in models:
                        if i['collected_in'] == 'LAB':
                            if i['receipt_for'] not in ['Refund','Cancelled']:
                                if 'cash' in mode_search:
                                    result['data'][2]['cash'] += i['amount_cash']
                                    result['cash_amount'] += i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][2]['card'] += i['amount_card']
                                    result['card_amount'] += i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][2]['upi'] += i['upi_amount']
                                    result['upi_amount'] += i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][2]['bank_transfer'] += i['bank_transfer_amount']
                                    result['bank_amount'] += i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][2]['cheque'] += i['cheque_amount']
                                    result['cheque_amount'] += i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][2]['insurance'] += i['insurance_amount']
                                    result['insurance_amount'] += i['insurance_amount']
                            else:
                                if 'cash' in mode_search:
                                    result['data'][2]['cash'] -= i['amount_cash']
                                    result['cash_amount'] -= i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][2]['card'] -= i['amount_card']
                                    result['card_amount'] -= i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][2]['upi'] -= i['upi_amount']
                                    result['upi_amount'] -= i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][2]['bank_transfer'] -= i['bank_transfer_amount']
                                    result['bank_amount'] -= i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][2]['cheque'] -= i['cheque_amount']
                                    result['cheque_amount'] -= i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][2]['insurance'] -= i['insurance_amount']
                                    result['insurance_amount'] -= i['insurance_amount']
                            result['data'][2]['total'] = result['data'][2]['cash'] + result['data'][2]['card'] + result['data'][2]['upi'] + result['data'][2]['bank_transfer'] + result['data'][2]['cheque'] + result['data'][2]['insurance']
                        elif i['collected_in'] == 'FO LAB':
                            if i['receipt_for'] not in ['Refund','Cancelled']:
                                if 'cash' in mode_search:
                                    result['data'][4]['cash'] += i['amount_cash']
                                    result['cash_amount'] += i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][4]['card'] += i['amount_card']
                                    result['card_amount'] += i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][4]['upi'] += i['upi_amount']
                                    result['upi_amount'] += i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][4]['bank_transfer'] += i['bank_transfer_amount']
                                    result['bank_amount'] += i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][4]['cheque'] += i['cheque_amount']
                                    result['cheque_amount'] += i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][4]['insurance'] += i['insurance_amount']
                                    result['insurance_amount'] += i['insurance_amount']
                            else:
                                if 'cash' in mode_search:
                                    result['data'][4]['cash'] -= i['amount_cash']
                                    result['cash_amount'] -= i['amount_cash']
                                if 'card' in mode_search:
                                    result['data'][4]['card'] -= i['amount_card']
                                    result['card_amount'] -= i['amount_card']
                                if 'upi' in mode_search:
                                    result['data'][4]['upi'] -= i['upi_amount']
                                    result['upi_amount'] -= i['upi_amount']
                                if 'bank' in mode_search:
                                    result['data'][4]['bank_transfer'] -= i['bank_transfer_amount']
                                    result['bank_amount'] -= i['bank_transfer_amount']
                                if 'cheque' in mode_search:
                                    result['data'][4]['cheque'] -= i['cheque_amount']
                                    result['cheque_amount'] -= i['cheque_amount']
                                if 'insurance' in mode_search:
                                    result['data'][4]['insurance'] -= i['insurance_amount']
                                    result['insurance_amount'] -= i['insurance_amount']
                            result['data'][4]['total'] = result['data'][4]['cash'] + result['data'][4]['card'] + result['data'][4]['upi'] + result['data'][4]['bank_transfer'] + result['data'][4]['cheque'] + result['data'][4]['insurance']
                    if 'pharmacy' in models:
                        if i['collected_in'] == 'PHARMACY': 
                            # if i['receipt_type'] == 'IP':
                                if i['receipt_for'] not in ['Refund','Cancelled']:
                                    if 'cash' in mode_search:
                                        result['data'][3]['cash'] += i['amount_cash']
                                        result['cash_amount'] += i['amount_cash']
                                    if 'card' in mode_search:
                                        result['data'][3]['card'] += i['amount_card']
                                        result['card_amount'] += i['amount_card']
                                    if 'upi' in mode_search:
                                        result['data'][3]['upi'] += i['upi_amount']
                                        result['upi_amount'] += i['upi_amount']
                                    if 'bank' in mode_search:
                                        result['data'][3]['bank_transfer'] += i['bank_transfer_amount']
                                        result['bank_amount'] += i['bank_transfer_amount']
                                    if 'cheque' in mode_search:
                                        result['data'][3]['cheque'] += i['cheque_amount']
                                        result['cheque_amount'] += i['cheque_amount']
                                    if 'insurance' in mode_search:
                                        result['data'][3]['insurance'] += i['insurance_amount']
                                        result['insurance_amount'] += i['insurance_amount']
                                else:
                                    if 'cash' in mode_search:
                                        result['data'][3]['cash'] -= i['amount_cash']
                                        result['cash_amount'] -= i['amount_cash']
                                    if 'card' in mode_search:
                                        result['data'][3]['card'] -= i['amount_card']
                                        result['card_amount'] -= i['amount_card']
                                    if 'upi' in mode_search:
                                        result['data'][3]['upi'] -= i['upi_amount']
                                        result['upi_amount'] -= i['upi_amount']
                                    if 'bank' in mode_search:
                                        result['data'][3]['bank_transfer'] -= i['bank_transfer_amount']
                                        result['bank_amount'] -= i['bank_transfer_amount']
                                    if 'cheque' in mode_search:
                                        result['data'][3]['cheque'] -= i['cheque_amount']
                                        result['cheque_amount'] -= i['cheque_amount']
                                    if 'insurance' in mode_search:
                                        result['data'][3]['insurance'] -= i['insurance_amount']
                                        result['insurance_amount'] -= i['insurance_amount']
                                result['data'][3]['total'] = result['data'][3]['cash'] + result['data'][3]['card'] + result['data'][3]['upi'] + result['data'][3]['bank_transfer'] + result['data'][3]['cheque'] + result['data'][3]['insurance']
                        elif i['collected_in'] == 'FO PH': 
                            # if i['receipt_type'] == 'IP':
                                if i['receipt_for'] not in ['Refund','Cancelled']:
                                    if 'cash' in mode_search:
                                        result['data'][5]['cash'] += i['amount_cash']
                                        result['cash_amount'] += i['amount_cash']
                                    if 'card' in mode_search:
                                        result['data'][5]['card'] += i['amount_card']
                                        result['card_amount'] += i['amount_card']
                                    if 'upi' in mode_search:
                                        result['data'][5]['upi'] += i['upi_amount']
                                        result['upi_amount'] += i['upi_amount']
                                    if 'bank' in mode_search:
                                        result['data'][5]['bank_transfer'] += i['bank_transfer_amount']
                                        result['bank_amount'] += i['bank_transfer_amount']
                                    if 'cheque' in mode_search:
                                        result['data'][5]['cheque'] += i['cheque_amount']
                                        result['cheque_amount'] += i['cheque_amount']
                                    if 'insurance' in mode_search:
                                        result['data'][5]['insurance'] += i['insurance_amount']
                                        result['insurance_amount'] += i['insurance_amount']
                                else:
                                    if 'cash' in mode_search:
                                        result['data'][5]['cash'] -= i['amount_cash']
                                        result['cash_amount'] -= i['amount_cash']
                                    if 'card' in mode_search:
                                        result['data'][5]['card'] -= i['amount_card']
                                        result['card_amount'] -= i['amount_card']
                                    if 'upi' in mode_search:
                                        result['data'][5]['upi'] -= i['upi_amount']
                                        result['upi_amount'] -= i['upi_amount']
                                    if 'bank' in mode_search:
                                        result['data'][5]['bank_transfer'] -= i['bank_transfer_amount']
                                        result['bank_amount'] -= i['bank_transfer_amount']
                                    if 'cheque' in mode_search:
                                        result['data'][5]['cheque'] -= i['cheque_amount']
                                        result['cheque_amount'] -= i['cheque_amount']
                                    if 'insurance' in mode_search:
                                        result['data'][5]['insurance'] -= i['insurance_amount']
                                        result['insurance_amount'] -= i['insurance_amount']
                                result['data'][5]['total'] = result['data'][5]['cash'] + result['data'][5]['card'] + result['data'][5]['upi'] + result['data'][5]['bank_transfer'] + result['data'][5]['cheque'] + result['data'][5]['insurance']
                            # else:
                            #     if i['receipt_for'] != 'Refund' and  i['receipt_for'] != 'Cancelled':
                            #         if 'cash' in mode_search:
                            #             result['data'][4]['cash'] += i['amount_cash']
                            #             result['cash_amount'] += i['amount_cash']
                            #         if 'card' in mode_search:
                            #             result['data'][4]['card'] += i['amount_card']
                            #             result['card_amount'] += i['amount_card']
                            #         if 'upi' in mode_search:
                            #             result['data'][4]['upi'] += i['upi_amount']
                            #             result['upi_amount'] += i['upi_amount']
                            #         if 'bank' in mode_search:
                            #             result['data'][4]['bank_transfer'] += i['bank_transfer_amount']
                            #             result['bank_amount'] += i['bank_transfer_amount']
                            #         if 'cheque' in mode_search:
                            #             result['data'][4]['cheque'] += i['cheque_amount']
                            #             result['cheque_amount'] += i['cheque_amount']
                            #         if 'insurance' in mode_search:
                            #             result['data'][4]['insurance'] += i['insurance_amount']
                            #             result['insurance_amount'] += i['insurance_amount']
                            #     else:
                            #         if 'cash' in mode_search:
                            #             result['data'][4]['cash'] -= i['amount_cash']
                            #             result['cash_amount'] -= i['amount_cash']
                            #         if 'card' in mode_search:
                            #             result['data'][4]['card'] -= i['amount_card']
                            #             result['card_amount'] -= i['amount_card']
                            #         if 'upi' in mode_search:
                            #             result['data'][4]['upi'] -= i['upi_amount']
                            #             result['upi_amount'] -= i['upi_amount']
                            #         if 'bank' in mode_search:
                            #             result['data'][4]['bank_transfer'] -= i['bank_transfer_amount']
                            #             result['bank_amount'] -= i['bank_transfer_amount']
                            #         if 'cheque' in mode_search:
                            #             result['data'][4]['cheque'] -= i['cheque_amount']
                            #             result['cheque_amount'] -= i['cheque_amount']
                            #         if 'insurance' in mode_search:
                            #             result['data'][4]['insurance'] -= i['insurance_amount']
                            #             result['insurance_amount'] -= i['insurance_amount']
                            #     result['data'][4]['total'] = result['data'][4]['cash'] + result['data'][4]['card'] + result['data'][4]['upi'] + result['data'][4]['bank_transfer'] + result['data'][4]['cheque'] + result['data'][4]['insurance']
            
            result['total_amount'] = result['cash_amount'] + result['card_amount'] + result['upi_amount'] + result['bank_amount'] + result['cheque_amount'] + result['insurance_amount']

            if export_type == 'pdf':
                flowobj = []
                print_config = PrintConfiguration.objects.get(clinic_id=clinic_id,print_type__report_type='Dayend Report Print')
                portrait_a4 = landscape_a4 = portrait_a5 = landscape_a5 = False
                if print_config.print_size == 'A4' and print_config.ortantation == 'Portrait':
                    portrait_a4 = True
                    hu,huh,huw,fu,fuh,fuw = 26.7,2.4,19.0,0,1.3,19
                    li1,lih,liw = 0.8,2,20
                    fw,fh,h,fp = 1.2,1.6,19,1.6
                    he,le,d,dl = 10.3,26,14,25.5
                    font,f1 = 10,8
                    orientation = portrait(A4)
                elif print_config.print_size == 'A4' and print_config.ortantation == 'Landscape':
                    landscape_a4 = True
                    li1,lih,liw = 1,1.8,28.6
                    hu,huh,huw,fu,fuh,fuw = 17.9,2.4,27.6,0,1.2,27.6
                    fw,fh,h,fp = 1.2,1.4,25,1.4
                    he,le,d,dl = 13.5,17.2,20.8,16.7
                    font,f1 = 10,8
                    orientation = landscape(A4)
                elif print_config.print_size == 'A5' and print_config.ortantation == 'Portrait':
                    portrait_a5 = True
                    li1,lih,liw = 0.8,1.8,14
                    hu,huh,huw,fu,fuh,fuw = 18.9,1.8,13,0,1.2,13
                    fw,fh,h,fp = 1.4,1.4,12,1.4
                    he,le,d,dl = 7.5,18.2,9,17.5
                    font,f1 = 8,7
                    orientation = portrait(A5)
                elif print_config.print_size == 'A5' and print_config.ortantation == 'Landscape':
                    landscape_a5 = True
                    li1,lih,liw = 0.8,1.5,20
                    hu,huh,huw,fu,fuh,fuw = 13,1.7,19.0,0,1,19.0
                    fw,fh,h,fp = 1.2,1.2,18,1.2
                    he,le,d,dl = 9.5,12,13,11.5
                    font,f1 = 9,7
                    orientation = landscape(A5)
                clinic_detail = Clinic.objects.get(clinic_id=clinic_id)
                header_url = 'https://picsum.photos/200/300'
                if clinic_detail.clinic_header_url:  
                    header_url = get_presigned_url(key=clinic_detail.clinic_header_url) if print_config.is_header else ''
                footer_url = 'https://picsum.photos/200/300'
                if clinic_detail.clinic_footer_url:
                    footer_url = get_presigned_url(key=clinic_detail.clinic_footer_url) if print_config.is_footer else ''

                if header_url == '':
                    x = 2 * cm  
                    top_margin = 1 * cm + (print_config.header_spacer_hight * cm) if print_config.header_spacer_hight else 0
                    bottom_margin = 2* cm + (print_config.footer_spacer_hight * cm) if print_config.footer_spacer_hight else 0 
                    if portrait_a5 and landscape_a5:
                        top_margin = 0.6 * cm + (print_config.header_spacer_hight * cm) if print_config.header_spacer_hight else 0
                        bottom_margin = 1.5* cm + (print_config.footer_spacer_hight * cm) if print_config.footer_spacer_hight else 0 
                else:
                    x = 0 * cm
                    if portrait_a5:
                        top_margin = 3.5 * cm
                        bottom_margin = 2 *cm
                    if portrait_a4:
                        top_margin = 4.2 * cm
                        bottom_margin = 2 *cm
                    if landscape_a5:
                        top_margin = 3.2 * cm
                        bottom_margin = 1.5 *cm
                    if landscape_a4:
                        top_margin = 4.2 * cm
                        bottom_margin = 2 *cm

                styles = getSampleStyleSheet()
                styles.add(ParagraphStyle( name='mystyle1' ,fontSize=10,fontName='Helvetica-Bold',alignment=TA_RIGHT))
                styles.add(ParagraphStyle( name='mystyle2' ,fontSize=10,fontName='Helvetica-Bold',spaceBefore=5,spaceAfter=8))
                if portrait_a5:
                    styles.add(ParagraphStyle( name='mystyle3' ,fontSize=8,fontName='Helvetica',alignment=TA_LEFT))
                else:
                    styles.add(ParagraphStyle( name='mystyle3' ,fontSize=10,fontName='Helvetica',alignment=TA_LEFT))
                styles.add(ParagraphStyle( name='mystyle4' ,fontSize=10,fontName='Helvetica',alignment=TA_CENTER))

                def firstpage(canvas,doc):
                    if header_url != "":
                        canvas.drawImage(header_url,cm,hu*cm,width=huw*cm,height=huh*cm,mask='auto')                                 
                    if footer_url != "":
                        canvas.drawImage(footer_url,cm,fu,width=fuw*cm,height=fuh*cm,mask='auto')

                    canvas.setFont('Helvetica-Bold',f1)
                    canvas.line(li1 * cm,lih * cm ,liw * cm,lih * cm )
                    canvas.drawString(fw*cm,fh*cm,"Printed By {} On {} | {}".format('request.user.login_name',datetime.now().date().strftime('%d-%m-%Y'),datetime.now().time().strftime('%I:%M %p')))
                    canvas.drawRightString(h * cm,fp * cm ,"Page {}".format(canvas.getPageNumber()))
                    canvas.setFont('Helvetica-Bold',12)
                    canvas.drawCentredString(he* cm,le * cm + x,"Day-End-Status Report") 

                    if from_date and to_date:
                        canvas.setFont('Helvetica',font)
                        new_from_date = (datetime.strptime(from_date, '%Y-%m-%d').date()).strftime('%d-%m-%Y')
                        new_to_date = (datetime.strptime(to_date, '%Y-%m-%d').date()).strftime('%d-%m-%Y')

                        if start_time and end_time:
                            new_start_time = (datetime.strptime(start_time,"%H:%M:%S").time()).strftime("%I:%M %p")
                            new_end_time = (datetime.strptime(end_time,"%H:%M:%S").time()).strftime("%I:%M %p")
                            canvas.drawString(d+5.5*cm,dl*cm  + x, f"From: {new_from_date} {new_start_time} - To: {new_to_date} {new_end_time}")
                        else:
                            canvas.drawString(d*cm,dl*cm + x, f"From: {new_from_date} - To: {new_to_date}")
    
                def laterpage(canvas,doc):
                    if print_config.header_all_page:
                        if header_url != "":
                            canvas.drawImage(header_url,0.8*cm,hu*cm,width=huw*cm,height=huh*cm,mask='auto')  
                    if print_config.footer_all_page:                               
                        if footer_url != "":
                            canvas.drawImage(footer_url,0.8*cm,fu*cm,width=fuw*cm,height=fuh*cm,mask='auto')

                    canvas.setFont('Helvetica-Bold',f1)
                    canvas.line(li1 * cm,lih * cm ,liw * cm,lih * cm )
                    canvas.drawString(fw*cm,fh*cm,"Printed By {} On {} | {}".format('request.user.login_name',datetime.now().date().strftime('%d-%m-%Y'),datetime.now().time().strftime('%I:%M %p')))
                    canvas.drawRightString(h * cm,fp * cm ,"Page {}".format(canvas.getPageNumber()))
                    canvas.setFont('Helvetica-Bold',12)
                    canvas.drawCentredString(he* cm,le * cm + x,"Day-End-Status Report") 

                    if from_date and to_date:
                        canvas.setFont('Helvetica',font)
                        new_from_date = (datetime.strptime(from_date, '%Y-%m-%d').date()).strftime('%d-%m-%Y')
                        new_to_date = (datetime.strptime(to_date, '%Y-%m-%d').date()).strftime('%d-%m-%Y')

                        if start_time and end_time:
                            new_start_time = (datetime.strptime(start_time,"%H:%M:%S").time()).strftime("%I:%M %p")
                            new_end_time = (datetime.strptime(end_time,"%H:%M:%S").time()).strftime("%I:%M %p")
                            canvas.drawString(d+5.5*cm,dl*cm  + x, f"From: {new_from_date} {new_start_time} - To: {new_to_date} {new_end_time}")
                        else:
                            canvas.drawString(d*cm,dl*cm + x, f"From: {new_from_date} - To: {new_to_date}")

                    flowobj.append(Spacer(0,0.4 *cm))
                #------------------------------------------------------------------------------------------------------------------------------------------
                tableobj = []
                tableobj.append(['Department','Cash','Card','UPI','Bank','Cheque','Total','Credit'])
                for i in result['data']:
                    tableobj.append([Paragraph(i['bill_type'],styles['mystyle3']),
                                     Paragraph(str(int(Roundoff(float(i['cash'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(i['cash']))))),styles['mystyle3']),
                                     Paragraph(str(int(Roundoff(float(i['card'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(i['card']))))),styles['mystyle3']),
                                     Paragraph(str(int(Roundoff(float(i['upi'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(i['upi']))))),styles['mystyle3']),
                                     Paragraph(str(int(Roundoff(float(i['bank_transfer'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(i['bank_transfer']))))),styles['mystyle3']),
                                     Paragraph(str(int(Roundoff(float(i['cheque'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(i['cheque']))))),styles['mystyle3']),
                                     Paragraph(str(int(Roundoff(float(i['total'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(i['total']))))),styles['mystyle3']),
                                     Paragraph(str(int(Roundoff(float(i['credit_value'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(i['credit_value']))))),styles['mystyle3'])
                                     ])
                
                tableobj.append([Paragraph('Total',styles['mystyle3']),
                                 Paragraph(str(int(Roundoff(float(result['cash_amount'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(result['cash_amount']))))),styles['mystyle3']),
                                 Paragraph(str(int(Roundoff(float(result['card_amount'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(result['card_amount']))))),styles['mystyle3']),
                                 Paragraph(str(int(Roundoff(float(result['upi_amount'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(result['upi_amount']))))),styles['mystyle3']),
                                 Paragraph(str(int(Roundoff(float(result['bank_amount'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(result['bank_amount']))))),styles['mystyle3']),
                                 Paragraph(str(int(Roundoff(float(result['cheque_amount'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(result['cheque_amount']))))),styles['mystyle3']),
                                 Paragraph(str(int(Roundoff(float(result['total_amount'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(result['total_amount']))))),styles['mystyle3']),
                                 Paragraph(str(int(Roundoff(float(result['total_credit_value'])))) if currency.currency_type == 'USD' else formatinr(str(int(Roundoff(float(result['total_credit_value']))))),styles['mystyle3'])
                                 ])

                tablestyle = TableStyle([
                        ("ALIGN", (0,0),(-1,-1), 'LEFT'),
                        ('LINEBELOW', (0,0), (-1,-1), 0.25, colors.lightgrey),
                        ('LINEABOVE', (0,0), (-1,0), 0.25, colors.black),
                        ('LINEBELOW', (0,0), (-1,0), 0.25, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE',(0,0),(-1,-1),font),
                        ('FONT',(0,0),(-1,0),'Helvetica-Bold',font),
                        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ])
                if portrait_a4 or landscape_a5:
                    table = Table(tableobj,style=tablestyle,rowHeights=1.5*cm,colWidths=[2.2*cm,2.2*cm,2.2*cm,2.2*cm,2.2*cm,2.2*cm,2.2*cm,2.2*cm,2.2*cm])
                elif landscape_a4:
                    table = Table(tableobj,style=tablestyle,rowHeights=1.5*cm,colWidths=[3.4*cm,3.4*cm,3.1*cm,3.1*cm,3.1*cm,3.1*cm,3.1*cm,3.2*cm,3.2*cm])
                elif portrait_a5:
                    table = Table(tableobj,style=tablestyle,rowHeights=1.5*cm,colWidths=[1.8*cm,1.6*cm,1.6*cm,1.6*cm,1.6*cm,1.6*cm,1.6*cm,1.6*cm,1.4*cm])
                flowobj.append(table)
                #------------------------------------------------------------------------------------------------------------------------------------------
                flowobj.append(Spacer(0,0.2 *cm))
                column_header = []
                tableobj1 = []
                tableobj1.append(["Credit Bills Split Up","","",""])
                tableobj1.append(['Department','Credit Type','Provider Name','Amount'])
                for i in credit_invoice_data:
                    if i['credit_type'] == 'Corprate credit':
                        i['credit_type'] = 'Corporate Credit'
                        provider_name = i['corporate_name']
                    elif i['credit_type'] == 'Insurance credit':
                        i['credit_type'] = 'Insurance Credit'
                        provider_name = i['company_name']
                    elif i['credit_type'] == 'Patient credit':
                        i['credit_type'] = 'Patient Credit'
                        provider_name = '-'
                    else:
                        i['credit_type'] = '-'
                        provider_name = '-'

                    tableobj1.append([Paragraph(str(i['module']) if i['module'] not in column_header else '',styles['mystyle3']),
                                     Paragraph(str(i['credit_type'] if i['credit_type'] else ''),styles['mystyle3']),
                                     Paragraph(str(provider_name),styles['mystyle3']),
                                     Paragraph(str(i['pending_amount']) if currency.currency_type == 'USD' else formatinr(str(int((Roundoff(float(i['pending_amount'])))))) ,styles['mystyle3'])])

                    if i['module'] not in column_header:
                        column_header.append(i['module'])
                tablestyle1 = TableStyle([
                        # ('SPAN',(0,2),(0,4)),
                        ('ALIGN', (0,0),(-1,-1), 'LEFT'),
                        ('GRID', (0,1), (-1,-1), 0.1, colors.lightgrey),
                        # ('FONTSIZE',(0,0),(-1,-1),font),
                        ('FONT',(0,0),(-1,-1),'Helvetica-Bold',font),
                        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                        ])
                
                if portrait_a4 or landscape_a5:
                    table1 = Table(tableobj1,style=tablestyle1,repeatRows=2,colWidths=[4.6*cm,4.6*cm,4.6*cm,4.6*cm])
                elif landscape_a4:
                    table1 = Table(tableobj1,style=tablestyle1,repeatRows=2,colWidths=[6.7*cm,6.7*cm,6.8*cm,6.8*cm])
                elif portrait_a5:
                    table1 = Table(tableobj1,style=tablestyle1,repeatRows=2,colWidths=[3.25*cm,3.25*cm,3.25*cm,3.25*cm])
                flowobj.append(table1)

                #------------------------------------------------------------------------------------------------------------------------------------------
                if cancel_invoice_data:
                    flowobj.append(Spacer(0,0.2 *cm))
                    tableobj2 = []
                    tableobj2.append(["Cancelled Bills","",""])
                    tableobj2.append(['Department','Count','Amount'])
                    for i in cancel_invoice_data:
                        tableobj2.append([Paragraph(str(i['module']),styles['mystyle3']),
                                        Paragraph(str(i['bill_count']),styles['mystyle3']),
                                        Paragraph(str(i['cancelled_amount']) if currency.currency_type == 'USD' else formatinr(str(int((Roundoff(float(i['cancelled_amount'])))))) ,styles['mystyle3'])])

                    tablestyle2 = TableStyle([
                            ('ALIGN', (0,0),(-1,-1), 'LEFT'),
                            ('GRID', (0,1), (-1,-1), 0.1, colors.lightgrey),
                            ('FONT',(0,0),(-1,-1),'Helvetica-Bold',font),
                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                            ])
                    
                    if portrait_a4 or landscape_a5:
                        table2 = Table(tableobj2,style=tablestyle2,repeatRows=2,colWidths=[6.7*cm,4.7*cm,6.7*cm])
                    elif landscape_a4:
                        table2 = Table(tableobj2,style=tablestyle2,repeatRows=2,colWidths=[10*cm,7*cm,10*cm])
                    elif portrait_a5:
                        table2 = Table(tableobj2,style=tablestyle2,repeatRows=2,colWidths=[5.1*cm,3*cm,5.1*cm])
                    flowobj.append(table2)

                    tablestyle3 = TableStyle([
                            ('ALIGN', (0,0),(-1,-1), 'LEFT'),
                            ('FONT',(0,0),(-1,-1),'Helvetica-Bold',font),
                            ('GRID', (0,0), (-1,-1), 0.1, colors.lightgrey),
                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                            ])
                
                    tableobj3 = []
                    tableobj3.append([Paragraph("* Pharmacy in Cancelled Bills Displays Return Bills Only.",styles['mystyle3'])])
                    if portrait_a4 or landscape_a5:
                        table3 = Table(tableobj3,colWidths=[18*cm])
                    elif landscape_a4:
                        table3 = Table(tableobj3,colWidths=[27*cm])
                    elif portrait_a5:
                        table3 = Table(tableobj3,colWidths=[13.5*cm])
                    flowobj.append(table3)
                #------------------------------------------------------------------------------------------------------------------------------------------

                response = HttpResponse(content_type = 'application/pdf')
                doc = SimpleDocTemplate(response,pagesize=orientation,rightMargin=0.8* cm,leftMargin=0.8 * cm,topMargin=top_margin,bottomMargin=bottom_margin,title='Day End Report',author='eMedHub.com')   
                doc.build(flowobj,onFirstPage=firstpage, onLaterPages=laterpage)
                return response
            response_time = time.time()
            response_time_log =response_time - api_start_time
            if response_time_log > 2.00:
                api_logger.info('DayEnd Report :{}'.format(response_time_log))
            return Response({'status':'success','message':'Day end bill report','data':result})
        
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again later'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 





op_credit = InpatientBillingSummary.objects.filter(clinic_id=clinic_id,bill_type__in=['credit'],invoice_date__date=date).values_list('id',flat=True)

credit_amount_final = 0
ins_credit_amount_final = 0
corp_credit_amount_final 
exempted_ids = []
op_history_manager = get_history_manager_for_model(InpatientBillingSumma
for ids in op_credit:
    try:
        op_first_version_values = op_history_manager.filter(
                                                    id=ids,
                                                    history_date__date=date,
                                                    # history_type='~',
                                                ).latest('history_dat
        if op_first_version_values.credit_type == 'Insurance credit':
            ins_credit_amount_final += op_first_version_values.net_amount - op_first_version_values.received_amount
        elif op_first_version_values.credit_type == 'Corprate credit':
            corp_credit_amount_final += op_first_version_values.net_amount - op_first_version_values.received_amount
        else:
            credit_amount_final += op_first_version_values.net_amount - op_first_version_values.received_amo
    except :
        exempted_ids.append(ids)
        pass
        














# >-----------------------------------------------------------------------------------------------------------------------
    data = request.GET
            clinic_id=request.clinic_id
            branch_id=data.get('branch_id')
            patient_id=data.get('patient_id')
            ip_admission_id=data.get('ip_admission_id')
            ip_search_data = {}
            search_data_1 = {}

            if ip_admission_id:
                ip_search_data['ip_admission_id']=ip_admission_id
                search_data_1['ip_number_id']=ip_admission_id
            ip_bills = InpatientBillingSummary.objects.filter(~Q(bill_type='cancelled'),Q(**search_data_1),clinic_id=clinic_id,patient_id=patient_id,bill_type__in=['regular','credit']).aggregate(total_bill=Coalesce(Sum('net_amount',output_field=IntegerField()),0),total_paid=Coalesce(Sum('received_amount',output_field=IntegerField()),0)) 
            lab_bills = LabBillSummary.objects.filter(~Q(bill_type='cancelled'),Q(**ip_search_data),clinic_id=clinic_id,patient_id=patient_id,bill_type__in=['regular','credit']).aggregate(total_bill=Coalesce(Sum('net_amount',output_field=IntegerField()),0),total_paid=Coalesce(Sum('received_amount',output_field=IntegerField()),0))
            currency = Configuration.objects.get(clinic_id=clinic_id)
            config = CustomConfig.objects.get(clinic_id=clinic_id) 
            
            pharmacy_bills=0
            if config.show_pharmacy_bills_in_fo:
                pharmacy_bills = PharmacyBillSummary.objects.filter(Q(**ip_search_data),clinic_id=clinic_id,patient_id=patient_id).aggregate(total_bill=Coalesce(Sum('net_amount',output_field=IntegerField(),filter=Q(bill_type__in=['Bill','Credit'])),0) - Coalesce(Sum('net_amount',output_field=IntegerField(),filter=Q(bill_type__in=['Return'])),0),total_paid=Coalesce(Sum('received_amount',output_field=IntegerField(),filter=Q(bill_type__in=['Bill','Credit'])),0) - Coalesce(Sum('received_amount',output_field=IntegerField(),filter=Q(bill_type__in=['Return'])),0))

            # tptal_receipt = BillingReceiptNumber.objects.filter(branch_id=branch_id,patient_id=patient_id,receipt_type='IP',module_id=ip_admission_id).values('paid_for').annotate(total=Coalesce(Sum('amount_received',output_field=IntegerField(),filter=Q(receipt_for__in=['Bill','Advance'])),0) - Coalesce(Sum('amount_received',output_field=IntegerField(),filter=Q(receipt_for__in=['Refund','Cancelled'])),0))
            
            receipts = BillingReceiptNumber.objects.filter(branch_id=branch_id,patient_id=patient_id,receipt_type='IP',module_id=ip_admission_id).values('paid_for','receipt_for','amount_received','op_amount','ip_amount','lab_amount','ph_amount')
            advance_receipt = ip_receipt = lab_receipt = pharmacy_receipt = 0
            for r in receipts:
                if 'IP' in r['paid_for']:
                    if r['receipt_for'] == 'Advance':
                        advance_receipt+=r['amount_received']
                # if 'IP' in r['paid_for']:
                #     if r['receipt_for'] == 'Bill':
                #         ip_receipt+=r['ip_amount']
                #     elif r['receipt_for'] == 'Cancelled':
                #         ip_receipt-=r['ip_amount']
                # elif 'LAB' in r['paid_for']:
                #     if r['receipt_for'] == 'Bill':
                #         lab_receipt+=r['lab_amount']
                #     else:
                #         lab_receipt-=r['lab_amount']
                # elif 'PHARMACY' in r['paid_for']:
                #     if r['receipt_for'] == 'Bill':
                #         pharmacy_receipt+=r['ph_amount']
                #     else:
                #         pharmacy_receipt-=r['ph_amount']


            approx_room_cost = 0
            room_change_detail = RoomChangeDetails.objects.filter(clinic_id=clinic_id, ip_admission_id=ip_admission_id,is_active=True).order_by('-created_date')
            room_change_details = room_change_detail[0] if room_change_detail else None

            credit_limit = CustomConfig.objects.filter(clinic_id=clinic_id).values('ip_credit_limit')

            module_ip = None
            if credit_limit:
                module_ip = next((item for item in credit_limit[0]['ip_credit_limit'] if item["module"] == "IP Room Charge Auto Billing"), None) 
            if module_ip and not module_ip['allow_overdue']:
                if room_change_details and not room_change_details.to_date:
                    ward = WardConfig.objects.get(clinic_id=clinic_id,ward_name__iexact=room_change_details.ward_name,is_active=True)
                    room_change_time = datetime.now()
                    room_start_time = datetime.combine(datetime.strptime(room_change_details.from_date.strftime('%Y-%m-%d'),'%Y-%m-%d').date(),datetime.strptime(room_change_details.from_time.strftime('%H:%M:%S'),'%H:%M:%S').time())
                    if room_change_details.is_hourly:
                        duration = round(((room_change_time - room_start_time).days)*24 + (((room_change_time - room_start_time).seconds)/60)/60,2)
                        hourly_amount = list(map(lambda x : {'hour':int(re.findall('[0-9]+',x['hourType'])[0]),'amount':x['total']},ward.hourly_rent))
                        sorted_time_amount = sorted(hourly_amount,key=lambda d:d['hour'])
                        if duration > 24:
                            total_amount = 0
                            net_amount = 0
                            days = duration / 24
                            stayed_days = int(str(days).split('.')[0])
                            exact_days = duration - (stayed_days * 24)
                            if exact_days != 0:
                                res = next(x for x, val in enumerate(sorted_time_amount)
                                        if val['hour'] >= exact_days)
                                net_amount = sorted_time_amount[res]['amount']
                            for j in sorted_time_amount:
                                if int(j['hour']) == 24:
                                    total_amount = j['amount']
                            approx_room_cost  =  (stayed_days * total_amount) + net_amount
                        else:
                            res = next(x for x, val in enumerate(sorted_time_amount)
                                    if val['hour'] >= duration)
                            approx_room_cost = sorted_time_amount[res]['amount']
                    else:
                        if room_change_details.is_attender == True :
                            # duration = (room_change_time - room_start_time).days
                            # duration1 = (((room_change_time - room_start_time).seconds)/60)/60
                            # if duration1:
                            #     duration += 1
                            duration = (room_change_time.date() - (room_start_time.date() - timedelta(days=1))).days
                            if ward and ward.attender_rent:
                                approx_room_cost = duration * ward.attender_rent['total']
                        else:    
                            # duration = (room_change_time - room_start_time).days
                            # duration1 = (((room_change_time - room_start_time).seconds)/60)/60
                            # if duration1:
                            #     duration += 1
                            duration = (room_change_time.date() - (room_start_time.date() - timedelta(days=1))).days
                            if ward and ward.day_rent:
                                approx_room_cost = duration * ward.day_rent['total']
                    
            #         response_data['approx_room_charge']=approx_room_cost
            # else:
            #     response_data['approx_room_charge'] = 0

            ip_admission = IpAdmissionDetails.objects.get(id=ip_admission_id)
            try:
                ip_admission_bill = IpAdmissionBillDetails.objects.get(ip_admission_id=ip_admission_id)
            except:
                return Response({'status': 'fail', 'message': 'No Bills Found For This Admission'}, status=status.HTTP_400_BAD_REQUEST)
            
            modified_date = update_date_time_in_pdf(config=config, admission=ip_admission, invoice=ip_admission_bill, invoice_date_key="bill_date")
            typee,sts = PrintType.objects.get_or_create(report_type='IP Approx Bill Print')
            print_config,sts = PrintConfiguration.objects.get_or_create(print_type_id=typee.id,clinic_id=clinic_id)
            clinic_detail = Clinic.objects.get(clinic_id=clinic_id)
            portrait_a4 = landscape_a4 = portrait_a5 = landscape_a5 = False
            if print_config.print_size == 'A4' and print_config.ortantation == 'Portrait':
                portrait_a4 = True
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l0,l11,l12,l13 = 25.6,25.6,24.9,24.2,23.5,22.8,22.2,24.4,23.7,23,22.2,21.6,21
                la1,la2,la3,la4,la5 = 1,4.2,11.3,15.5,10.5
                li1,li2,li3,li4,li5 = 2.2,26.2,21.6,20.8,21.5
                hu,huh,huw,fu,fuh,fuw = 26.5,2.7,19.0,0,1.5,19.0
                bar,bw,bh = 15,5.7,1.0
                lw,b,h,fw,fp,pp = 20,24.9,26.6,1.8,19,2.4
                font,f1 = 10,8
                wmx,wmy,wmf = 3,0.5,80
                rotate = 50
                orientation = portrait(A4)
            elif print_config.print_size == 'A4' and print_config.ortantation == 'Landscape':
                landscape_a4 = True
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l0,l11,l12,l13 = 16.8,16.8,16.1,15.4,14.7,14,13.4,15.6,14.9,14.2,12.9,12.8,12.2
                la1,la2,la3,la4,la5 = 1.2,4.7,15.5,19.7,13.5
                li1,li2,li3,li4,li5 = 2.0,17.5,13.1,12.5,12.5
                hu,huh,huw,fu,fuh,fuw = 17.9,2.4,27.6,0,1.2,27.6
                bar,bw,bh = 14.9,5.7,1.0
                lw,b,h,fw,fp,pp = 28.6,16.1,17.8,1.6,26,2.2
                font,f1 = 10,8
                wmx,wmy,wmf = 3,1,80
                rotate = 30
                orientation = landscape(A4)
            elif print_config.print_size == 'A5' and print_config.ortantation == 'Portrait':
                portrait_a5 = True
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l0 ,l11,l12,l13 = 18,18.4,17.9,17.3,16.8,16.2,15.6,17.3,16.7,16.1,15,15,14.4
                la1,la2,la3,la4,la5 = 1.1,3.8,8.5,11.2,7.5
                li1,li2,li3,li4,li5 = 1.6,18.9,15.5,15.1,14.8
                hu,huh,huw,fu,fuh,fuw = 18.9,1.8,13,0,1.2,13
                bar,bw,bh = 9,5.7,1.0
                lw,b,h,fw,fp,pp = 14,17.8,19,1.3,19,1.9
                font,f1 = 8,7
                wmx,wmy,wmf = 3,0.5,50
                rotate = 40
                orientation = portrait(A5)
            elif print_config.print_size == 'A5' and print_config.ortantation == 'Landscape':
                landscape_a5 = True
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l0,l11,l12,l13 = 12.1,12.1,11.5,10.9,10.5,9.9,9.5,11.1,10.5,9.9,8.9,9.1,8.5
                la1,la2,la3,la4,la5 = 1.2,4.2,11.3,15.5,9.5
                li1,li2,li3,li4,li5 = 1.5,12.9,9.4,9,8.3
                hu,huh,huw,fu,fuh,fuw = 13,1.7,19.0,0,1,19.0
                bar,bw,bh = 10.8,5.7,1.0
                lw,b,h,fw,fp,pp = 20,11.8,13.1,1.2,19,1.8
                font,f1 = 8,7
                wmx,wmy,wmf = 3,0.5,50
                rotate = 30
                orientation = landscape(A5)
            patient_age = ""
            if ip_admission.patient.dob:
                patient_age = patient_appointment_age(ip_admission.patient.dob, ip_admission.admission_date)
            elif ip_admission.patient.approx_dob:
                patient_age = patient_appointment_age(ip_admission.patient.approx_dob, ip_admission.admission_date)

            consultant_name = ''
            if ip_admission.doctor:
                if ip_admission.doctor.title:
                    consultant_name += ip_admission.doctor.title + ' '
                if ip_admission.doctor.first_name:
                    consultant_name += ip_admission.doctor.first_name + ' '
                if ip_admission.doctor.qualifications:
                    consultant_name += ip_admission.doctor.qualifications

            flowobj =[]
            header_url = ''#https://picsum.photos/200/300'
            if clinic_detail.ip_header_url:  
                header_url = get_presigned_url(key=clinic_detail.ip_header_url) if print_config.is_header else ''
            footer_url = ''#https://picsum.photos/200/300'
            if clinic_detail.ip_footer_url:
                footer_url = get_presigned_url(key=clinic_detail.ip_footer_url) if print_config.is_footer else ''
            z=0 * cm
            if header_url == '':
                x = 2 * cm  
                if portrait_a4:
                    z=print_config.header_spacer_hight * cm
                    top_margin=6.8*cm + print_config.header_spacer_hight * cm
                if portrait_a5:
                    top_margin = 4.6 * cm + print_config.header_spacer_hight * cm
                    z=print_config.header_spacer_hight * cm
                if landscape_a5:
                    top_margin = 4.3 * cm + print_config.header_spacer_hight * cm
                    z=print_config.header_spacer_hight * cm
                if landscape_a4:
                    top_margin = 6.8 * cm + print_config.header_spacer_hight * cm
                    z=print_config.header_spacer_hight * cm
            else:
                if portrait_a5:
                    top_margin = 7 * cm
                if portrait_a4:
                    top_margin = 9.2 * cm
                if landscape_a5:
                    top_margin = 6.8 * cm
                if landscape_a4:
                    top_margin = 9.2 * cm
                x = -0.5 * cm
            bottom_margin = print_config.footer_spacer_hight * cm if not print_config.is_footer else 1.2*inch

            patient_name = ''
            if ip_admission.patient:
                if ip_admission.patient.title:
                    patient_name += ip_admission.patient.title + ' '
                if ip_admission.patient.first_name:
                    patient_name += ip_admission.patient.first_name + ' '
                if ip_admission.patient.middle_name:
                    patient_name += ip_admission.patient.middle_name + ' '
                if ip_admission.patient.last_name:
                    patient_name += ip_admission.patient.last_name
                if ip_admission.patient.initial:
                    patient_name += '.' + ip_admission.patient.initial
            address_1 = ''
            if ip_admission.patient.address_line_1:
                if len(ip_admission.patient.address_line_1) > 32:
                    address_1 += ip_admission.patient.address_line_1[:30] + ' ..'
                else:
                    address_1 += ip_admission.patient.address_line_1
            address_2 = ''
            if ip_admission.patient.address_line_2:
                if len(ip_admission.patient.address_line_2) > 32:
                    address_2 += ":  "
                    address_2 += ip_admission.patient.address_line_2[:30] + ' ..'
                else:                # flowobj.append(Spacer(0,0.8 *cm))
                    address_2 += ":  "
                    address_2 += ip_admission.patient.address_line_2
            address_3 =''
            if address_2:
                if ip_admission.patient.city or ip_admission.patient.pincode:
                    address_3 += ':  '
                    address_3 += "{} {}".format(ip_admission.patient.city.city_name if ip_admission.patient.city else '',ip_admission.patient.pincode if ip_admission.patient.pincode else '')
            else:
                if ip_admission.patient.city or ip_admission.patient.pincode:
                    address_2 += ':  '
                    address_2 += "{}{}".format(ip_admission.patient.city.city_name if ip_admission.patient.city else '',ip_admission.patient.pincode if ip_admission.patient.pincode else '')
            try:
                corporate = CorpotatePatientLink.objects.get(patient_id=ip_admission.patient_id,is_active=True).employer.company_name
                insurance = ip_admission.patient.insurance_company_name
            except:
                corporate = ''
                insurance = ip_admission.patient.insurance_company_name
            corporate_insurance = ''
            if corporate and ip_admission.primary_payment_type == 'Corprate credit':
                corporate_insurance += corporate
            if insurance and ip_admission.primary_payment_type == 'Insurance credit':
                corporate_insurance += insurance

            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle( name='mystyle1' ,fontSize=font,fontName='Helvetica-Bold',alignment=TA_CENTER))
            styles.add(ParagraphStyle( name='mystyle2' ,fontSize=font,fontName='Helvetica',alignment=TA_LEFT))
            styles.add(ParagraphStyle( name='mystyle3' ,fontSize=font,fontName='Helvetica',alignment=TA_RIGHT))
            styles.add(ParagraphStyle( name='mystyle4' ,fontSize=font,fontName='Helvetica',alignment=TA_CENTER))
            styles.add(ParagraphStyle( name='mystyle5' ,fontSize=font,fontName='Helvetica-Bold',alignment=TA_RIGHT))
            styles.add(ParagraphStyle( name='mystyle6' ,fontSize=font,fontName='Helvetica-Bold',alignment=TA_LEFT))

            def firstpage(canvas,doc):
                if header_url != "":
                    canvas.drawImage(header_url,0.8*cm,hu*cm,width=huw*cm,height=huh*cm,mask='auto')                                 
                if footer_url != "":
                    canvas.drawImage(footer_url,0.8*cm,fu*cm,width=fuw*cm,height=fuh*cm,mask='auto')
                canvas.setFont('Helvetica-Bold',f1)
                canvas.line(0.8 * cm,li1 * cm ,lw * cm,li1 * cm )
                canvas.drawString(1 * cm,pp * cm ,"Printed By {} On {}".format(request.user.login_name,datetime.now().date().strftime('%d-%m-%Y')))
                canvas.drawString(1 * cm,fw * cm ,"For Billing And General Enquiry, Please Contact Us @ {}".format(clinic_detail.clinic_name))
                canvas.drawRightString(fp * cm,fw * cm ,"Page {}".format(canvas.getPageNumber()))                

                barcode_data = barcode.get_barcode_class('code128')
                barcode_data.default_writer_options['write_text'] = False
                barcode_file = barcode_data(str(ip_admission.patient.patient_account_number), writer= ImageWriter())
                barcodes = barcode_file.save('barcode')

                canvas.setLineWidth(0.8)
                canvas.line(0.8 * cm,li2 * cm + x -z,lw * cm,li2 * cm + x -z)

                canvas.setFont('Helvetica',font)
                canvas.drawString(la1* cm,l2 * cm + x -z,"Patient Name ")
                canvas.drawString(la1* cm,l3 * cm + x -z,"UHID")
                canvas.drawString(la1* cm,l4 * cm + x -z,"Mobile No ")
                canvas.drawString(la1* cm,l5 * cm + x -z,"Address ")
                canvas.drawString(la1* cm,l12 * cm + x-z,"Room Number")
                canvas.drawString(la1* cm,l13 * cm + x-z,"Insurance/Corporate")
                
                canvas.drawString(la2* cm,l2 * cm + x -z,":  {} ({}/{})".format(patient_name.upper(),patient_age,ip_admission.patient.gender.upper()))
                canvas.drawString(la2* cm,l3 * cm + x -z,":  {}".format(ip_admission.patient.patient_account_number if ip_admission.patient.patient_account_number else ""))
                canvas.drawString(la2* cm,l4 * cm + x -z,":  {}".format(ip_admission.patient.mobile_number if ip_admission.patient.mobile_number else ""))
                canvas.drawString(la2* cm,l5 * cm + x -z,":  {}".format(address_1.upper() if address_1 else ''))
                canvas.drawString(la2* cm,l6 * cm + x -z,"{}".format(address_2.upper() if address_2 else ''))
                canvas.drawString(la2* cm,l7 * cm + x -z,"{}".format(address_3.upper() if address_3 else ''))
                canvas.drawString(la2* cm,l12 * cm + x-z,":  {} ".format(room_change_detail[0].room_number if room_change_detail else ''))        
                canvas.drawString(la2* cm,l13 * cm + x-z,":  {} ".format(corporate_insurance)) 

                canvas.drawString(la3* cm,l4 * cm + x -z,"Invoice Date")
                canvas.drawString(la3* cm,l5 * cm + x -z,"Invoice Number")
                canvas.drawString(la3* cm,l6 * cm + x -z,"IP Number")
                canvas.drawString(la3* cm,l7 * cm + x  -z,"IP Admission Date")
                # canvas.drawString(la3* cm,l12 * cm + x-z,"Discharged On")
                
                canvas.drawImage(barcodes,bar*cm,b*cm + x -z,width=bw*cm,height=bh*cm,mask='auto')
                os.remove(barcodes)
                canvas.drawString(la4* cm,l5 * cm + x-z,":  {}".format(ip_admission_bill.bill_number if ip_admission_bill.bill_number else "-"))
                canvas.drawString(la4* cm,l4 * cm + x-z,":  {}".format(modified_date["invoice"]["invoice_date"]))
                canvas.drawString(la4* cm,l6 * cm + x-z,":  {}".format(ip_admission.ip_number if ip_admission.ip_number else "-"))
                canvas.drawString(la4* cm,l7 * cm + x-z,":  {}".format(modified_date["admission"]["admission_date"]))
                # canvas.drawString(la4* cm,l12 * cm + x-z,":  {} {}".format(ip_admission.discharge_date.strftime('%d-%m-%Y') if ip_admission.discharge_date else '',ip_admission.discharge_time.strftime('%I:%M %p') if ip_admission.discharge_time else ''))
                canvas.setFont('Helvetica-Bold',font)
                flowobj.append(Spacer(0,0.4 *cm))
                canvas.drawCentredString(la5* cm,h * cm + x-z,"APPROXIMATE BILL REPORT")
            tableobj = []
            tableobj1 = []
            total_bill_amt = 0
            total_paid_amount = 0
            total_balance_amount = 0
            tableobj.append([Paragraph('S.No',styles['mystyle6']),Paragraph('Module',styles['mystyle6']),Paragraph('Bill Amount',styles['mystyle5'])])
            n=0
            if ip_bills:
                n+=1
                total_bill_amt+=ip_bills['total_bill']
                total_paid_amount+=ip_bills['total_paid']
                # total_balance_amount += ip_bills-ip_receipt
                tableobj.append([n,Paragraph('IP',styles['mystyle2']),Paragraph(str(ip_bills['total_bill']) if currency.currency_type == 'USD' else formatinr(str(ip_bills['total_bill'])),styles['mystyle3'])])
            if lab_bills:
                n+=1
                total_bill_amt+=lab_bills['total_bill']
                total_paid_amount += lab_bills['total_paid']
                # total_balance_amount += lab_bills['total_bill']-lab_bills['total_paid']
                tableobj.append([n,Paragraph('LAB',styles['mystyle2']),Paragraph(formatinr(str(lab_bills['total_bill'])) if currency.currency_type == 'USD' else formatinr(str(lab_bills['total_bill'])),styles['mystyle3'])])
            if config.show_pharmacy_bills_in_fo:
                if pharmacy_bills:
                    n+=1
                    total_bill_amt+=pharmacy_bills['total_bill']
                    total_paid_amount += pharmacy_bills['total_paid']
                    # total_balance_amount += pharmacy_bills['total_bill']-pharmacy_bills['total_paid']
                    tableobj.append([n,Paragraph('PHARMACY',styles['mystyle2']),Paragraph(str(pharmacy_bills['total_bill']) if currency.currency_type == 'USD' else formatinr(str(pharmacy_bills['total_bill'])),styles['mystyle3'])])
            # if advance_receipt:
            #     n+=1
            #     total_paid_amount += advance_receipt
            #     tableobj.append([n,Paragraph('Advance',styles['mystyle2']),Paragraph(str('-'),styles['mystyle3']),Paragraph(str(advance_receipt),styles['mystyle3']),Paragraph(str('-'),styles['mystyle3'])])
            if approx_room_cost:
                n+=1
                total_bill_amt+=approx_room_cost
                # total_balance_amount += approx_room_cost
                tableobj.append([n,Paragraph('Approx. Room Charges',styles['mystyle2']),Paragraph(str(approx_room_cost) if currency.currency_type == 'USD' else formatinr(str(approx_room_cost)),styles['mystyle3'])])
            total_balance_amount = total_bill_amt - total_paid_amount
            tablestyle = TableStyle([
                    ("ALIGN", (0,0),(-1,-1), 'LEFT'),
                    # ("ALIGN", (-1,0),(-1,0), 'RIGHT'),
                    ('LINEABOVE', (0,0), (-1,0), 0.25, colors.black),
                    ('LINEBELOW', (0,0), (-1,0), 0.25, colors.black),
                    ('LINEBELOW', (0,-1), (-1,-1), 0.25, colors.black),
                    ('FONTSIZE',(0,0),(-1,-1),10),
                    ('FONT',(0,0),(-1,1),'Helvetica-Bold',10),
                    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ])
            if portrait_a4 or landscape_a5:
                table = Table(tableobj,style=tablestyle,repeatRows=1,colWidths=[2*cm,5.3*cm,11.9*cm]) 
                range1,range2,range3,range4,range5 = 120,11,25,5,6
            elif landscape_a4:
                table = Table(tableobj,style=tablestyle,repeatRows=1,colWidths=[5*cm,9*cm,14*cm])
                range1,range2,range3,range4,range5 = 205,12,26,6,7
            elif portrait_a5:
                table = Table(tableobj,style=tablestyle,repeatRows=1,colWidths=[1.4*cm,2.9*cm,9.1*cm])  
                range1,range2,range3,range4,range5 = 90,8,22,2,3
            flowobj.append(table)
            appro_amt = total_bill_amt - (total_paid_amount + ip_admission_bill.total_balance)  
            flowobj.append(Spacer(0, 0.3*cm))
            flowobj.append(Paragraph('{}Approx. Bill Amount  {}: {}'.format('&nbsp;'*range1, '&nbsp;'*range2, str(round(decimal.Decimal(total_bill_amt),2)) if currency.currency_type == 'USD' else formatinr(str(round(decimal.Decimal(total_bill_amt),2)))),styles['mystyle6']))
            flowobj.append(Spacer(0, 0.2*cm))
            flowobj.append(Paragraph('{}Paid Amount{}: {}'.format('&nbsp;'*range1, '&nbsp;'*range3, str(total_paid_amount + ip_admission_bill.total_balance) if currency.currency_type == 'USD' else formatinr(str(total_paid_amount + ip_admission_bill.total_balance))),styles['mystyle6']))
            flowobj.append(Spacer(0, 0.2*cm))
            if appro_amt > 0:
                range1 = range1-6
                flowobj.append(Paragraph('{}Approx. Receivable Amount{}: {}'.format('&nbsp;'*range1, '&nbsp;'*range4, str(appro_amt) if currency.currency_type == 'USD' else formatinr(str(appro_amt))),styles['mystyle6']))
            else:
                flowobj.append(Paragraph('{}Approx. Refund Amount{}: {}'.format('&nbsp;'*range1, '&nbsp;'*range5, str(abs(appro_amt)) if currency.currency_type == 'USD' else formatinr(str(abs(appro_amt)))),styles['mystyle6']))
            response = HttpResponse(content_type = 'application/pdf')
            doc = SimpleDocTemplate(response,pagesize=orientation,rightMargin=1* cm, leftMargin=1 * cm,topMargin=top_margin, bottomMargin=bottom_margin,title='IP Approx Bill Report Report',author='eMedHub.com')   
            doc.build(flowobj,onFirstPage=firstpage)
            return response

        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({"status": "fail", "message": "Something went wrong. Please try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)