# ==============================================================================
# Group class:
# member fields:
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
# ==============================================================================

S_ALONE = 0
S_TALKING = 1

class Group:

    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0

    def join(self, name):
        self.members[name] = S_ALONE
        return

    def is_member(self, name):
        # IMPLEMENTATION
        # ---- start your code ---- #
        return name in self.members
        # ---- end of your code --- #

    # implement
    def leave(self, name):
        """
        leave the system, and the group
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        if name in self.members:
            del self.members[name]
            
        for k, v in list(self.chat_grps.items()):
            if name in v:
                v.remove(name)
                # If only one person is left, they are alone now
                if len(v) == 1:
                    self.members[v[0]] = S_ALONE
                    del self.chat_grps[k]
                # If group is empty, clean it up
                elif len(v) == 0:
                    del self.chat_grps[k]
        return
        # ---- end of your code --- #


    def find_group(self, name):
        """
        Auxiliary function internal to the class; return two
        variables: whether "name" is in a group, and if true
        the key to its group
        """
        found = False
        group_key = 0
        # IMPLEMENTATION
        # ---- start your code ---- #
        for k, v in self.chat_grps.items():
            if name in v:  # FIXED: name in list, not list in string
                found = True
                group_key = k
                break
        # ---- end of your code --- #
        return found, group_key

    def connect(self, me, peer):
        """
        me is alone, connecting peer.
        if peer is in a group, join it
        otherwise, create a new group with you and your peer
        """
        peer_in_group, group_key = self.find_group(peer)
        
        # IMPLEMENTATION
        # ---- start your code ---- #
        if peer_in_group:
            self.chat_grps[group_key].append(me)
        else:
            self.grp_ever += 1 # Use the class counter for unique keys
            new_key = self.grp_ever
            self.chat_grps[new_key] = [me, peer]
            
        # Update states to talking
        self.members[me] = S_TALKING
        self.members[peer] = S_TALKING
        # ---- end of your code --- #
        return

    # implement
    def disconnect(self, me):
        """
        find myself in the group, quit, but stay in the system
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        for k, v in list(self.chat_grps.items()):
            if me in v:
                v.remove(me)
                # If only one person left in group, disband it and set them to alone
                if len(v) == 1:
                    self.members[v[0]] = S_ALONE
                    del self.chat_grps[k]
                elif len(v) == 0:
                    del self.chat_grps[k]
                    
        # Update my state to alone
        if me in self.members:
            self.members[me] = S_ALONE
        # ---- end of your code --- #
        return

    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    # implement
    def list_me(self, me):
        """
        return a list, "me" followed by other peers in my group
        """
        my_list = []
        # IMPLEMENTATION
        # ---- start your code ---- #
        peer_in_group, group_key = self.find_group(me)
        if peer_in_group:
            my_list.append(me)
            for peer in self.chat_grps[group_key]:
                if peer != me:
                    my_list.append(peer)
        # ---- end of your code --- #
        return my_list


if __name__ == "__main__":
    g = Group()
    g.join('a')
    g.join('b')
    g.join('c')
    g.join('d')
    print("--- Joined ---")
    print(g.list_all())

    g.connect('a', 'b')
    print("--- a connects to b ---")
    print(g.list_all())
    
    g.connect('c', 'a')
    print("--- c connects to a ---")
    print(g.list_all())
    
    g.leave('c')
    print("--- c leaves ---")
    print(g.list_all())
    
    g.disconnect('b')
    print("--- b disconnects ---")
    print(g.list_all())