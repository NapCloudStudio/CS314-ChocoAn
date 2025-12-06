from http import server
import os
import linecache
import uuid
import datetime

from dao import DAO

def generate_reports():
    print("generating reports...")
    member_reports()
    provider_reports()
    move_old_service_records()

def member_reports():
    member_report_directory = "weeky_reports/member_reports/current"
    old_member_report_directory = "weeky_reports/member_reports/old"
    provider_report_directory = "provider_reports/current"

    os.makedirs(member_report_directory, exist_ok = True)
    os.makedirs(old_member_report_directory, exist_ok=True)
    data = DAO.chocan()

    for f in member_report_directory:
        src_path = os.path.join(member_report_directory, f)
        new_filename = uuid.uuid4() + f
        dst_path = os.path.join(old_member_report_directory, new_filename)
        os.rename(src_path, dst_path)

    
    for ifile_name in os.listdir(provider_report_directory):

        created = False

        if ifile_name.endswith(".txt"):
            
                member_id_line = linecache.getline(os.path.join(provider_report_directory, ifile_name), 2)
                extracted_member_id = [int(word) for word in member_id_line.split() if word.isdigit()]
                member_id = extracted_member_id[0]

                provider_id_line = linecache.getline(os.path.join(provider_report_directory, ifile_name), 1)
                extracted_provider_id = [int(word) for word in provider_id_line.split() if word.isdigit()]
                provider_id = extracted_provider_id[0]

                service_code_line = linecache.getline(os.path.join(provider_report_directory, ifile_name), 3)
                extracted_service_code = [int(word) for word in service_code_line.split() if word.isdigit()]
                service_code = extracted_service_code[0]

                time_line = linecache.getline(os.path.join(provider_report_directory, ifile_name), 0)
                time = time_line.replace("Date and Time", "Date of servie", 1)

                ofile_name = member_id
                ofile_name += ".txt"

                if os.path.exists(os.path.join(member_report_directory, ofile_name)):
                    created = True

                with open(os.path.join(member_report_directory, ofile_name), "at") as ofile:
                    if created == True:
                        name = data.get_member_name(member_id)
                        address = data.get_member_addr(member_id)
                        street = data.get_addr_street(address)
                        city = data.get_addr_city(address)
                        state = data.get_addr_state(address)
                        zipcode = data.get_addr_zip(address)

                        ofile.write(f"Member name: {name}\n")
                        ofile.write(f"Member number {member_id}\n")
                        ofile.write(f"Member street address {street}\n")
                        ofile.write(f"Member city: {city}\n")
                        ofile.write(f"Member state: {state}\n")
                        ofile.write(f"Member zip code {zipcode}\n\n")

                    provider_name = data.get_provider_name(provider_id)
                    service_name = data.get_service_name(service_code)

                    ofile.write(f"\t{time}\n")
                    ofile.write(f"\tProvider name: {provider_name}\n")
                    ofile.write(f"\tService name: {service_name}\n\n")

def provider_reports():
    provider_report_directory = "weekly_reports/provider_reports/current"
    old_provider_report_directory = "weekly_reports/provider_reports/old"
    service_report_directory = "provider_reports/current"
    ETF_directory = "weekly_reports/ETFs/current"
    old_ETF_directory = "weekly_reports/ETFs/old"
    manager_report_directory = "weekly_reports/manager_reports"

    os.makedirs(provider_report_directory, exist_ok = True)
    os.makedirs(old_provider_report_directory, exist_ok = True)
    os.makedirs(ETF_directory, exist_ok = True)
    os.makedirs(old_ETF_directory, exist_ok = True)
    os.makedirs(manager_report_directory, exist_ok = True)

    data = DAO.chocan()

    id_list = data.get_provider_ids()
    provider_total_fees = dict.fromkeys(id_list, 0)
    provider_total_consultations = dict.fromkeys(id_list, 0)

        

    for f in provider_report_directory:
            src_path = os.path.join(provider_report_directory, f)
            new_filename = uuid.uuid4() + f
            dst_path = os.path.join(old_provider_report_directory, new_filename)
            os.rename(src_path, dst_path)

    for f in ETF_directory:
            src_path = os.path.join(ETF_directory, f)
            new_filename = uuid.uuid4() + f
            dst_path = os.path.join(old_ETF_directory, new_filename)
            os.rename(src_path, dst_path)

    for ifile_name in os.listdir(service_report_directory):
            report_created = False
            ETF_created = False

            if ifile_name.endswith(".txt"):

                member_id_line = linecache.getline(os.path.join(service_report_directory, ifile_name), 2)
                extracted_member_id = [int(word) for word in member_id_line.split() if word.isdigit()]
                member_id = extracted_member_id[0]

                provider_id_line = linecache.getline(os.path.join(service_report_directory, ifile_name), 1)
                extracted_provider_id = [int(word) for word in provider_id_line.split() if word.isdigit()]
                provider_id = extracted_provider_id[0]

                service_code_line = linecache.getline(os.path.join(service_report_directory, ifile_name), 3)
                extracted_service_code = [int(word) for word in service_code_line.split() if word.isdigit()]
                service_code = extracted_service_code[0]

                time_line = linecache.getline(os.path.join(service_report_directory, ifile_name), 0)
                time = time_line.replace("Date and Time", "Date of service", 1)

                ofile_name = provider_id
                ofile_name += ".txt"


                member_name = data.get_member_name(member_id)
                service_fee = data.get_service_fee(service_code)

                provider_total_consultations[provider_id] += 1
                provider_total_fees[provider_id] += service_fee

                if os.path.exists(os.path.join(provider_report_directory, ofile_name)):
                    report_created = True

                with open(os.path.join(provider_report_directory, ofile_name), "at") as ofile:
                    if report_created == True:
                        provider_name = data.get_provider_name(provider_id)
                        provider_address = data.get_provider_addr(provider_id)
                        provider_street = data.get_addr_street(provider_address)
                        provider_city = data.get_addr_city(provider_address)
                        provider_state = data.get_addr_state(provider_address)
                        provider_zipcode = data.get_addr_zip(provider_address)

                        ofile.write(f"Provider name: {provider_name}\n")
                        ofile.write(f"Provider number: {provider_id}\n")
                        ofile.write(f"Provider street address: {provider_street}\n")
                        ofile.write(f"Provider city: {provider_city}\n")
                        ofile.write(f"Provider state: {provider_state}\n")
                        ofile.write(f"Provider zip code: {provider_zipcode}\n\n")

                    ofile.write(f"\t{time}\n")
                    ofile.write(f"\tMember name: {member_name}\n")
                    ofile.write(f"\tMember number: {member_id}\n")
                    ofile.write(f"\tServicecode: {service_code}\n")
                    ofile.write(f"\tFee to be paid: ${service_fee}\n\n")

    for key in provider_total_fees:
                ofile_name = key
                ofile_name += ".txt"
                with open(os.path.join(provider_report_directory, ofile_name), "at") as ofile:
                    ofile.write(f"Total number of consultations with members: {provider_total_consultations[key]}\n")
                    ofile.write(f"Total fee for the week: ${provider_total_fees[key]}\n")

                ETF_file_name = provider_id
                ETF_file_name += ".txt"

                with open(os.path.join(ETF_directory, ETF_file_name), "wt") as ETF_file:
                    ETF_file.write(f"{provider_total_fees[key]}")

    manager_report_filename = uuid.uuid1()
    manager_report_filename += ".txt"

    with open(os.path.join(manager_report_directory, manager_report_filename), "wt") as ofile:
        provider_count = 0
        service_count = 0
        total_fee = 0
        for key in provider_total_fees:
            if provider_total_consultations[key] != 0:
                provider_count += 1
                service_count += provider_total_consultations[key]
                total_fee += provider_total_fees[key]

                ofile.write(f"Provider id: {key}\n")
                ofile.write(f"\tTotal consultations: {provider_total_consultations[key]}\n")
                ofile.write(f"\tFee: ${provider_total_fees[key]}\n\n")

        ofile.write(f"Number of providers: {provider_count}")
        ofile.write(f"Total number of consultations: {service_count}")
        ofile.write(f"total fee: {total_fee}")

def move_old_service_records():
    current_directory = "provider_reports/current"
    old_directory = "provider_reports/old"

    for f in current_directory:
            src_path = os.path.join(current_directory, f)
            dst_path = os.path.join(old_directory, f)
            os.rename(src_path, dst_path)